# ! python3
# Deleting Unneeded files - write a program to search for a file thats larger
# than 100 MB and then  delete it.
# Note:- Send2trash module sends the file to recycle bin

import send2trash
import os


def delete_files(location):
    os.path.abspath(location)

    for foldername, subfolders, filenames in os.walk(location):

        for file in filenames:
            size = os.path.getsize(foldername + '\\' + file)
            if int(size) >= 100000000:
                # uncomment the code after testing
                # send2trash.send2trash(file)
                print('Deleting %s...' % file)


if __name__ == '__main__':
    delete_files(location='C:\\Users\\palla')
