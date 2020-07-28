# ! python3
# backup_to_zip.py - Copies an entire folder and its contents into
# a ZIP whose filename increments.

import zipfile
import os


def back_up_to_zip(folder):
    # Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1
    print('Creating %s...' % zip_filename)
    back_up_zip = zipfile.ZipFile(zip_filename, 'w')

    for foldernames, subfolder, filenames in os.walk(folder):
        print('Adding files in %s' % foldernames)
        back_up_zip.write(foldernames)

        for filename in filenames:
            new_dir = os.path.dirname(folder)
            new_dir + '\\' + os.path.basename(folder) + '/'
            if filename.startswith(new_dir) and filename.endswith('.zip'):
                continue
            back_up_zip.write(os.path.join(foldernames, filename))
    back_up_zip.close()
    print('Done')


if __name__ == '__main__':
    back_up_to_zip('C:\\delicious')
