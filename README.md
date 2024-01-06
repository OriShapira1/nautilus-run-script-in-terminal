# Nautilus run script in terminal
A nautilus context menu extension meant to open a script (.sh) in the gnome terminal

## Installation from Source
### Installing the Dependencies
Simply copy and paste the appropriate command for your distro:

| Distro | Command|
|--------|--------|
| Fedora | ``` $ sudo dnf install nautilus-python python3-gobject ``` |
| Debian >= 12 | ``` $ sudo apt install python3-nautilus python3-gi ``` |
| Ubuntu | ``` $ sudo apt-get install python-nautilus python3-gi ``` |
| Arch Linux | ``` $ sudo pacman -S python-gobject python-nautilus ``` |

### Installing the Extension
Clone the repository:
```
git clone https://github.com/OriShapira1/nautilus-run-script-in-terminal
```

Copy the file/s to the appropriate folder, creating it if needed:
```bash
$ mkdir ~/.local/share/nautilus-python
$ mkdir ~/.local/share/nautilus-python/extensions
$ cp nautilus-openscriptinterminal.py ~/.local/share/nautilus-python/extensions/
```

Restart Nautilus and the extension will be available:
```bash
$ nautilus -q
```

If that doesn't work try logging out and back in. 

## Optional - configure settings
#### Only files with execution permissions
Files without execution permissions will not trigger the context menu.
In the Python file change check_perms from False to True:
```python
class config():

    ...

    check_perms = True
```
#### Only files with a secret key appended to them
Files without the secret key will not trigger the context menu - avoids accidentally running untrusted scripts
In the Python file change SECRET_KEY to the desired key:
```python
class config():

    SECRET_KEY = 'Your-desired-key'
```
Choose how many lines to check for the SECRET_KEY from the end of the file (not including whitespace only lines):
```python
class config():

    ...

    lines_to_search_for_key = 20
```
