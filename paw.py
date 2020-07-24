import sys
import pyperclip

# ! python3

PASSWORDS = {'jio-fi': '7474774',
             'email': 'yryyryy',
             'luggage': '123'
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
