# bullet_point_adder.py - Adds wikipedia points to the start
# Of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# Separate lines and stars.
lines = text.split('\n')
for i in range(len(lines)):  # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
