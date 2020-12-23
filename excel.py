"""
This module handles the work of interacting with MSExcel files.
"""
import openpyxl

def get_active_sheet(ipath, lang='EN'):
    """
    opens the English language sheet
    """
    workbook = openpyxl.load_workbook(filename=ipath)
    return workbook[lang]

def get_link_target(sheet, cell):
    """Given a cell address, this function looks up the target of a link at
    that location.
    """
    cell = sheet[cell]
    return cell.hyperlink.target

def _is_empty(sheet, cell_address):
    """a helper for identifying empty cells by address
    """
    if _text(sheet, cell_address) is None:
        return True
    if len(_text(sheet, cell_address)) > 0:
        return False
    return True

def _cell(row, col):
    """convert x,y to a cell address
    """
    row = row+1
    col_letter = chr(ord('A') + col)
    return f"{col_letter}{row}"

def _coord(row, col):
    return f"{col.upper()}{row}"

def _text(sheet, cell_address):
    """returns the text of cell"""
    cell = sheet[cell_address]
    return cell.value

def _colnum(col):
    """translates a column address string into a column id"""
    col_id = 0
    multiple = 1
    for letter in col:
        temp = ord(letter) - ord('A') + 1
        col_id *= multiple
        multiple *= 26
        col_id += temp
    return col_id

def _rownum(row):
    """translates a row address string into a row id"""
    return int(row)

def get_table_header(sheet, x, y, width=2):
    """parses a line of cells to extract column headers"""
    column_names = []
    leftmost_column = x
    for col in range(leftmost_column, leftmost_column + width):
        column_names.append(_text(sheet, _cell(y, col)))
    return column_names

def get_table(sheet, x, y, width=2, contains_header=True):
    """parses a rectangle of cells to extract a table"""
    column_names = None
    if contains_header:
        column_names = get_table_header(sheet, x, y, width)
    else:
        column_names = [ f"Column {ii}" for ii in range(width)]
    leftmost_column = x
    values = []
    if contains_header:
        y += 1
    read_address = _cell(y, leftmost_column)
    while not _is_empty(sheet, read_address):
        row_vals = []
        for curr_col in range(leftmost_column, leftmost_column + width):
            read_address = _cell(y, curr_col)
            row_vals.append(_text(sheet, read_address))
        print(row_vals)
        if len(row_vals) > 0:
            values.append(dict(zip(column_names, row_vals)))
        y += 1
        read_address = _cell(y, leftmost_column)
    return values
