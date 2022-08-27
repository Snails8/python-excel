import openpyxl

wb = openpyxl.load_workbook("/tmp/test.xlsx")\


print([[cell.value for cell in row] for row in wb['Sheet1']['A1:C5']])