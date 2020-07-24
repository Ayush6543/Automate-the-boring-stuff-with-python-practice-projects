import re

text = '''  ayush3Kumar
Ayush33kumar
Ayushkumar33
   AyushkuMar4
AyushKumar55
'''

def password_tester(words):
    pattern = re.compile(r'[a-zA-Z0-9]{8}.*')
    matches = pattern.findall(words)
    print('Passwords are: ')
    for match in matches:
        print(match.strip())


password_tester(text)
