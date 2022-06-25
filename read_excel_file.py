import xlrd


def read_xl_file():
    CD_L =[]
    #loc = ("Power_view_files.xlsx")
    loc = ("C:\\Users\\talla\\Desktop\\External\\SF_file Details3.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    #print("-----------"+cel_data)
    for i in range(sheet.nrows):
     CD_L.append((sheet.cell_value(i, 0)))
    return CD_L
print(read_xl_file())