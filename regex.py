import os
import re

dirs = os.listdir('C:\\Users\\palla\\PycharmProjects\\Automate')
pattern = re.compile(r'.*?\.txt')

for dire in dirs:
    matches = pattern.findall(dire)
    for match in matches:
        print(match)
