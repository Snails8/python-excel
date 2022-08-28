

def sheet1(ws) :
    ws["A1"] = "hoge"


    # C列
    for i in range(1, 10):
        ws.cell(row = 2+i, column = 3).value(i)
