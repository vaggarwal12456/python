import xlwt
import datetime
p1 = xlwt.easyxf("font:name TimesNewRoman, color-index red, bold on",num_format_str="#,##0.00")
p2 = xlwt.easyxf(num_format_str = "DD-MM-YY")
wb = xlwt.Workbook()
ws1 = wb.add_sheet("Sheet1",cell_overwrite_ok=True)
ws1.write(0,0,1,p1)
ws1.write(0,1,2,p1)
ws1.write(0,2,1234.5678,p1)
ws1.write(1,0,datetime.datetime.now(),p2)
ws1.write(2,2,xlwt.Formula("A1 + B1"),p1)
wb.save("first.xlsx")
