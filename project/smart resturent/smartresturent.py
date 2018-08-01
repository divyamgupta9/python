import xlrd
import xlwt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
price=0
n=1
def orde():
    global price
    global n
    order=input("ENTER ID OF FOOD : ")
    if(order=='no'):
           ws.write(n,3,price)
           ws.write(n,2,"GRAND TOTAL")
           bill.save('bill.xls')
           noorder()
    else:
        for k in range(1,7,1):
            if(order==rs.cell_value(k,2)):
               cost=int(rs.cell_value(k,1))
               qty=int(input("SELECT THE QUANTITY OF FOOD : "))
               #print(type(qty))
               price=price+(cost*qty)
               print(price)
               ws.write(n,0,rs.cell_value(k,3))
               ws.write(n,1,cost)
               ws.write(n,2,qty)
               ws.write(n,3,(cost*qty))       
               n+=1
               orde()
        
        
def noorder():
    global n
    print("THANK YOU")
    rb=xlrd.open_workbook('bill.xls')
    rs=rb.sheet_by_index(0)
    for i in range(0,n+1,1):
        for j in range(0,4,1):
            print(rs.cell_value(i,j),end='  ')
        print("\n")
    print("\n YOUR BILL IS",price,"Rs.")
    mail()

def mail():
    fromaddr = "divyamgupta0501@gmail.com"
    toaddr = "divyam0501g@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Fodd bill."
    body = "Your bill is"
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("bill.xls", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="bill.xls"')
    msg.attach(part)
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "password")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
print("        MENUE")
rb=xlrd.open_workbook('div.xls')
rs=rb.sheet_by_index(0)
bill=xlwt.Workbook()
ws=bill.add_sheet("Sheet 1")
ws.write(0,0,"FOOD")
ws.write(0,1,"PRICE")
ws.write(0,2,"QTY")
ws.write(0,3,"TOTAL")
for i in range(0,7,1):
    for j in range(0,4,1):
            print(rs.cell_value(i,j),end='  ')
    print("\n")
per=input("Do you wanna order : ")
if(per=='yes'):
	orde()	
elif(per=='no'):
    noorder()

