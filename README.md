# Nautilus run script in terminal
A nautilus context menu extension meant to open a script (.sh) in the gnome terminal

## How to install 
#### clone the repository to your home folder:
```
git clone https://github.com/OriShapira1/nautilus-run-script-in-terminal
```

#### Create a folder for the extensions if you don't have one already:
```
mkdir ~/.local/share/nautilus-python
mkdir ~/.local/share/nautilus-python/extensions
cp ./nautilus-run-script-in-terminal.py  ~/.local/share/nautilus-python/extensions
```
## Optional - configure settings
#### Only files with execution permissions
Files without execution permissions will not trigger the context menu.
In the Python file change check_perms from False to True:
```
class config():

    ...

    check_perms = True
```
#### Only files with a secret key appended to them
Files without the secret key will not trigger the context menu - avoids accidentally running untrusted scripts
In the Python file change SECRET_KEY to the desired key:
```
class config():

    SECRET_KEY = 'Your-desired-key'
```
Choose how many lines to check for the SECRET_KEY from the end of the file (not including whitespace only lines):
```
class config():

    ...

    lines_to_search_for_key = 20
```
