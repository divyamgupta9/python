import xlwt
a=xlwt.Workbook()
b=a.add_sheet("Sheet 1")
for i in range(0,7,1):
                for j in range(0,4,1):
                        print ("row",i,"col",j)
                        c=input()
                        b.write(i,j,c)
a.save('div.xls')
