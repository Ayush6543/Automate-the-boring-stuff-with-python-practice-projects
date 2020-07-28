# ! python3
# Filling in the gaps- Find all files with a given prefix such as spam00.txt
# in a single folder and looks for any gaps and rename all the files later.

import os
import shutil
import re

file_pattern = re.compile(r'^(spam)(\d+)(.txt)')


def filling_in_the_gaps(location):
    for file in os.listdir(location):
        mo = file_pattern.search(file)

        if mo is None:
            continue

        first_group = mo.group(1)
        second_group = mo.group(2)
        third_group = mo.group(3)

        filename = first_group + second_group + third_group

        abs_dir = os.path.abspath('.')
        file = os.path.join(abs_dir, file)
        filename = os.path.join(abs_dir, filename)

        # shutil.move(file, filename)
        print('Renaming %s to "%s"...' % (file, filename))


if __name__ == '__main__':
    filling_in_the_gaps('C:\\Users\\palla\\PycharmProjects\\Automate\\automating_tasks\\chapter9')
