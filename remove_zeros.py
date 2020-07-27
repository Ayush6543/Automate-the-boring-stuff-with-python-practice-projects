# ! python3
# Removing zeros from filenames - spam00042.txt to spam42.txt

import re
import os
import shutil

file_pattern = re.compile(r'''^(.*?) # before part
([0]+)                               # zero digit
((.*?)?)                             # after zero
((\.txt)$)                           # only changing text files
''', re.VERBOSE)

for file in os.listdir('.'):
    mo = file_pattern.search(file)

    if mo is None:
        continue

    before_part = mo.group(1)
    num_part = mo.group(2)
    after_num = mo.group(4)
    txt_part = mo.group(5)

    zero_files = before_part + after_num + txt_part

    abs_dir = os.path.abspath('.')
    file = os.path.join(abs_dir, file)
    zero_files = os.path.join(abs_dir, zero_files)
    print('Renaming "%s to "%s"...' % (file, zero_files))
    # shutil.move(file, zero_files)
