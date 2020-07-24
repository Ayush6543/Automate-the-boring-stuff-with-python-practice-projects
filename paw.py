import sys
import pyperclip

# ! python3

PASSWORDS = {'jio-fi': 'ayushyadav123',
             'computer': 'ayushyadav123$',
             'gmail': 'yadavayush123$',
             'ms-office-account': 'yadavayush321$'
             }

if len(sys.argv) < 2:
    print('Don\'t try to be oversmart')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Passwords copied to clipboard for ' + account)
else:
    print('Invalid account' + account)
# @py.exe C:\Users\palla\Pycharm Projects\Automate\pythonbasics\paw.py
