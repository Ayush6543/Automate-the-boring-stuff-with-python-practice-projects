# ! python3
# Renaming dates from European style to American style.

import shutil
import os
import re

text = '11-2-2018'
date_pattern = re.compile(r'''^(.*?)
((0|1|2|3|4)?\d)-        # date
((0|1)?\d)-              # month
((19|20)\d\d)            # year 
(.*?)$
''', re.VERBOSE)

for filename in os.listdir('.'):
    mo = date_pattern.search(filename)

    if mo is None:
        continue

    before_part = mo.group(1)
    day_part = mo.group(2)
    month_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    amer_files = before_part + month_part + '-' + day_part + '-' + year_part + after_part

    abs_dir = os.path.abspath('.')
    filename = os.path.join(abs_dir, filename)
    amer_files = os.path.join(abs_dir, amer_files)

    # Rename the files to American styles.
    print('Rename "%s to "%s"...' % (filename, amer_files))
    # shutil.move(filename, amer_files)