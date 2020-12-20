import openpyxl

def get_active_sheet(ipath, lang='EN'):
    wb = openpyxl.load_workbook(filename=ipath)
    return wb[lang]

def get_link_target(sheet, cell):
    cell = sheet[cell]    
    return cell.hyperlink.target

def _coord(row, col):
    return f"{(col).upper()}{row}"

def _text(sheet, cell):
    cell = sheet[cell]    
    return cell.value

def _colnum(col):
    col_id = 0
    multiple = 1
    for cc in col:
        temp = ord(cc) - ord('A') + 1
        print(col_id, multiple, cc, temp )
        col_id *= multiple
        multiple *= 26
        col_id += temp
    return col_id

def get_table(sheet, row, column, width=2, header=True):
    column_names = []
    if header:
        for ii in range(column, column + width):
            column_names.append(_text(sheet, _coord(row, ii)))
    else:
        for ii in range(width):
            column_names.append(_text(sheet, _coord(row, ii)))
    return column_names
