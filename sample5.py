import xlwt
from xlrd import open_workbook

target_column = 0     # This example only has 1 column, and it is 0 indexed

book = open_workbook('voc.xlsx')
sheet = book.sheets()[0]
data = [sheet.row_values(i) for i in xrange(sheet.nrows)]
labels = data[0]    # Don't sort our headers
data = data[1:]     # Data begins on the second row
data.sort(key=lambda x: x[target_column])

bk = xlwt.Workbook()
sheet = bk.add_sheet(sheet.name)

for idx, label in enumerate(labels):
     sheet.write(0, idx, label)

for idx_r, row in enumerate(data):
    for idx_c, value in enumerate(row):
        sheet.write(idx_r+1, idx_c, value)

bk.save('result.xls')    # Notice this is xls, not xlsx like the original file is