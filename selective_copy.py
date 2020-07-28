# ! python3
# Selective copy- walk throught a directory folder tree and search for file
# with a certain extension (such as .pdf or .jpg)

import os
import shutil


def selective_copy(location):
    for __, __, filenames in os.walk(location):
        for file in filenames:
            if file.endswith('.txt'):
                # shutil.copytree('C:\\Users\\palla\\Music', 'C:\\copied_file')
                print('Copying a file %s to %s' % (file, 'C:\\copied_fiile'))


if __name__ == '__main__':
    selective_copy(location='C:\\Users\\palla\\Music')

