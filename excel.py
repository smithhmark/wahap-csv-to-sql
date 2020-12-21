import openpyxl

def get_active_sheet(ipath, lang='EN'):
    wb = openpyxl.load_workbook(filename=ipath)
    return wb[lang]

def get_link_target(sheet, cell):
    cell = sheet[cell]    
    return cell.hyperlink.target

def _is_empty(sheet, cell_address):
    if _text(sheet, cell_address) is None:
        return True
    if len(_text(sheet, cell_address)) > 0:
        return False
    return True

def _cell(y, x):
    """convert x,y to a cell address
    """
    row = y+1
    col_letter = chr(ord('A') + x)
    return f"{col_letter}{row}"

def _coord(row, col):
    return f"{col.upper()}{row}"

def _text(sheet, cell_address):
    cell = sheet[cell_address]    
    return cell.value

def _colnum(col):
    col_id = 0
    multiple = 1
    for cc in col:
        temp = ord(cc) - ord('A') + 1
        col_id *= multiple
        multiple *= 26
        col_id += temp
    return col_id

def _rownum(row):
    return int(row)

def get_table_header(sheet, x, y, width=2):
    column_names = []
    leftmost_column = x
    for col in range(leftmost_column, leftmost_column + width):
        column_names.append(_text(sheet, _cell(y, col)))
    return column_names

def get_table(sheet, x, y, width=2, contains_header=True):
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
