

def get_link_target(sheet, cell):
    cell = sheet[cell]    
    print(dir(cell))
    print(dir(cell.hyperlink))
    return cell.hyperlink.target

