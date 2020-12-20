import openpyxl

def get_active_sheet(ipath, lang='EN'):
    wb = openpyxl.load_workbook(filename=ipath)
    return wb[lang]

def get_link_target(sheet, cell):
    cell = sheet[cell]    
    return cell.hyperlink.target

