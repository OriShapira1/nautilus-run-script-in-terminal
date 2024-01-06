import gi
gi.require_version('Gtk', '4.0')

from gi.repository import Nautilus, GObject
from urllib.parse import urlparse, unquote
import subprocess
import os
from file_read_backwards import FileReadBackwards as frb

class config():

    SECRET_KEY = '' # set it to whatever you want

    # if enabled, the file will not be ran unless the key is present somewhere in the sh file
    require_secret_key = True
    lines_to_search_for_key = 20 # checked from the end of the file
    # if enabled, the file will not be ran unless the user has execution permissions to it
    check_perms = True

class MyItemExtension(GObject.GObject, Nautilus.MenuProvider):

    VALID_MIMETYPES = ('application/x-shellscript',)

    def get_file_items(self, files):
        
        # check that only one file selected
        if len(files) != 1:
            return ()
        # check that file is valid
        if  files[0].get_mime_type() not in self.VALID_MIMETYPES:
            return ()
        # check that file can be executed
        configz = config()
        if configz.check_perms == True:
            if not self.check_perms(files[0]):
                return ()

        # if configured to check for secret key, check for it
        if configz.require_secret_key == True:
            if not self.validate_secret_key(files[0], configz.SECRET_KEY, configz.lines_to_search_for_key):
                return ()
        
        item_copy_path = Nautilus.MenuItem(
            name='Nautilus::open_in_terminal',
            label='Run script in terminal',
            tip='Copy the full path to the clipboard'
        )
        item_copy_path.connect('activate', self.on_menu_item_clicked, files)

        return item_copy_path,


    def on_menu_item_clicked(self, item, files):
        filename = files[0].get_name()
        file_path = unquote(urlparse(files[0].get_uri()).path)
        # https://unix.stackexchange.com/questions/373186/open-gnome-terminal-window-and-execute-2-commands
        subprocess.Popen(f"gnome-terminal -t {filename} -- /bin/sh -c '{file_path};'", shell=True)
        
        
    def check_perms(self, file):
        file_path = unquote(urlparse(file.get_uri()).path)
        perms = oct(os.stat(file_path).st_mode)[-3:]
        for num in perms:
            if int(num) % 2 == 1:
                return True
        return False

    def validate_secret_key(self, fileprovided, s_key, cfglines):
        file_path = unquote(urlparse(fileprovided.get_uri()).path)
        with frb(file_path) as f:
            i = 0
            for line in f:
                if not line.isspace():
                    i += 1
                if i == cfglines - 1:
                    return False
                if line.find(s_key) != -1:
                    return True


