tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(table):
    col_width = [0] * len(table)
    count = 0
    while count < len(table):
        for item in table[count]:
            if len(item) > col_width[count]:
                col_width[count] = len(item)
        count += 1
    for i in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][i].rjust(col_width[item]), end=' ')
        print()


print_table(tableData)
# print(' ' * (max([len(e) for e in data]) - len(data[i])) + data[i], end=' ')
# data[i].rjust(8), end=' '

