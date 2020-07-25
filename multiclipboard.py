# ! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save<keyword> - Saves clipboard to keyboard
#        py.exe mcb.pyw <keyboard> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keyboards to clipboard.

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')


if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    if sys.argv[1].lower() == 'delete':
        if sys.argv[2]:
            del mcb_shelf[sys.argv[2]]
            pyperclip.copy('')
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for key in list(mcb_shelf.keys()):
            del mcb_shelf[key]
        pyperclip.copy('')
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])


mcb_shelf.close()
