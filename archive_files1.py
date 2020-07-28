# ! python3
"""Walk a directory and archieve files with certain extensions, such as
.txt or .py and nothing else"""


import os


def archive_files(folder):
    folder = os.path.abspath(folder)

    for foldernames , subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.txt'):
                print(filename)
            if filename.endswith('.py'):
                print(filename)


if __name__ == '__main__':
    archive_files('C:\\Users\\palla\\PycharmProjects\\Automate\\automating_tasks\\chapter9\\')
