# ! python3
import re
import pyperclip

regex_url = re.compile(r'''http(s)?://\w+\.(\w){2,4}''', re.VERBOSE)

text = str(pyperclip.paste())

group = []
for groups in regex_url.finditer(text):
    group.append(groups[0])

if len(group) > 0:
    pyperclip.copy('\n'.join(group))
    print('Copied to clipboard')
    print('\n'.join(group))
else:
    print('No url was found')
'''https://youtube.comandhttp://lynda.com or https://code.net'''
