from random import randint, random
import xlsxwriter

workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0

# iterating through content list
for i in range(1,101):
    worksheet.write(row, column, i)
    row += 1

workbook.close()