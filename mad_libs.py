import re


def mad_libs(mad_libs_file1, mad_libs_file2):
    pattern = re.compile(r'(NOUN|ADJECTIVE|VERB)')

    with open(mad_libs_file1, 'r') as input_file, open(mad_libs_file2, 'w') as output_file:
        contents = input_file.read()

        matches = pattern.findall(contents)

        for match in matches:
            sub = input('Enter a ' + match + ':')
            contents = contents.replace(match, sub, 1)

        output_file.write(contents)
        print(contents)


if __name__ == '__main__':
    mad_libs('mad_libs.txt', 'mad_libs3.txt')
