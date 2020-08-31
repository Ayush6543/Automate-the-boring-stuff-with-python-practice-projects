# ! python3
"""
blank_row_inserter.py- A program that inserts blank row in a spreadsheet
files.
"""
import openpyxl


def blank_row_inserter(n, m, location):
    wb = openpyxl.load_workbook('produceSales.xlsx')
    sheet = wb.get_sheet_by_name('Sheet')

    for row in range(1, int(n) - 1):
        for col in range(2, sheet.max_column - 1):
            sheet.insert_rows(row + (m + 1), col)
    wb.save(location)


if __name__ == '__main__':
    """
     After checking the program works properly. Add sys after each
     of the parameters down.
     """
    blank_row_inserter(n=int(input('index: ')), m=int(input('blank_rows: '))
                       , location=str(input('location: ')))
