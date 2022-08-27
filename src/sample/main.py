import openpyxl

wb = openpyxl.load_workbook("/tmp/test.xlsx")


# sheet1
ws = wb["Sheet1"]

ws["A1"] = "hoge"



# 保存
wb.save("/tmp/sample.xlsx")
