import xlrd
from seleniumdemo.Business import search
def login_data():
    workbook = xlrd.open_workbook('C:\\Users\\yinguohao\\Downloads\\测试账号表.xlsx')
    sheet = workbook.sheet_by_name("Sheet1")
    rows = sheet.nrows
    data1 = []
    for i in range(1,rows):
        line = sheet.row_values(i)
        data1.append(line)
    for a in range(len(data1)):
        search.sinitekwh_login(data1[a][0], str(data1[a][1]))
        # print(str(data1[a][0]))



print(login_data())