# ! python3
# Renaming all words.txt files to spam_words.txt

import shutil
import re
import os

prefix_pattern = re.compile(r'''^(.*?)
(\.txt)$
''', re.VERBOSE)

for filename in os.listdir('.'):
    mo = prefix_pattern.search(filename)

    if mo is None:
        continue

    before_part = mo.group(1)

    prefix_file = 'spam_' + before_part + '.txt'
    abs_working_dir = os.path.abspath('.')
    filename = os.path.join(abs_working_dir, filename)
    prefix_file = os.path.join(abs_working_dir, prefix_file)

    # Rename the files.
    print('Renaming "%s to "%s"' % (filename, prefix_file))
    # shutil.move(filename, prefix_file)
