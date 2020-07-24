# ! python3

import pyperclip
import re

credit_card = re.compile(r'^4[0-9]{12}(?:[0-9]{3})?$')

matches = []
text = str(pyperclip.paste())
for groups in credit_card.sub('\1*********', text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No credit card number or social security number found')
"""4222222222222"""
