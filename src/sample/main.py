from sheet1 import sheet1
import openpyxl

wb = openpyxl.load_workbook("/tmp/test.xlsx")


# sheet1
ws = wb["Sheet1"]

sheet1.sheet1(ws)

# 保存
wb.save("/tmp/sample.xlsx")
