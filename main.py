import os
import time
import colorama
from fpdf import FPDF
import questionary as qs
from colorama import Fore,Style

colorama.init(autoreset=False)

#####################Business information
business_name = "King Hardware"
business_address = ["123 Anywhere Street","Johannesburg,2001"]
contact_details = "011-012-3654/kinghardware@co.business.co.za"

####################Client Information
client_data = {}

client_name = qs.text("Name of Client: ").ask()


list_of_products = ["Steel Beams", "Planks", "Tiles","Pipes","Cables","Nails","Hammer","Tape"]

def price_calculation(item,quantity):
    prices = {"Steel Beams" : 200, "Planks": 100,
           "Tiles" : 50,"Pipes" : 40
           ,"Cables" : 150,"Nails":30,"Hammer":50,"Tape":15}
    price = prices[item]
    total_price = price * quantity
    return price,total_price

def vat_calculation(item):
    vat_percentage = 0.15
    return item * vat_percentage


number = int(qs.text("how many items: ").ask())
for i in range(number):
    items = qs.select("Select product: ", choices=list_of_products).ask()
    quantity = int(qs.text(f"How many {items}: ").ask())
    unit_price,gross_total_price = price_calculation(items,quantity)
    print()
    
    discount = qs.confirm("Discount? ").ask()
    if discount:
        discount_amount = int(qs.text("How much: ").ask())
        print()
        price_after_discount = gross_total_price - discount_amount
        vat = qs.confirm("Is VAT charged: ").ask()
        if vat:
            vat_price = vat_calculation(price_after_discount)
            net_total = price_after_discount + vat_price
        else:
            vat_price = 0
        client_data[f"item_{i}"] = {"item":items,"quantity":quantity,
                                    "unit price":unit_price,"sub total":gross_total_price,
                                    "discount":discount_amount,"vat":vat_price,"total":net_total}
    else:
        discount_amount = 0
        vat = qs.confirm("Is VAT charged: ").ask()
        if vat:
            vat_price = vat_calculation(gross_total_price)
            net_total = gross_total_price + vat_price
        else:
            vat_price = 0
            net_total = gross_total_price - vat_price
        client_data[f"item_{i}"] = {"item": items,"quantity": str(quantity),
                                    "unit price": str(unit_price),"sub total": str(gross_total_price),
                                    "discount": str(discount_amount),"vat": str(vat_price),"total": str(net_total)}

os.system("clear")
qs.press_any_key_to_continue("Press any key to generate").ask()
time.sleep(10)
os.system("clear")
print(f"{Fore.GREEN}{Style.BRIGHT}PDF Generated Successfully")
print("test liine")

sub_sub_total = 0
total_discount = 0
total_vat = 0
net_net_total = 0

for i in range(number):
    sub_sub_total += int(client_data[f"item_{i}"]["sub total"])

for i in range(number):
    total_discount += int(client_data[f"item_{i}"]["discount"])

for i in range(number):
    total_vat += float(client_data[f"item_{i}"]["vat"])


for i in range(number):
    net_net_total += float(client_data[f"item_{i}"]["total"])


class FPDF(FPDF):

    def header(self):
        self.set_font("Helvetica","UB",27)
        self.image("icons8-hardware-64.png")
        self.set_xy(40,12)
        self.cell(160,20,"INVOICE", align="C")
        self.set_xy(10,20)

    def footer(self) -> None:
        self.set_font("Helvetica", "B",10)
        self.set_xy(10,287)
        self.cell(0,7,contact_details, align="C")


####################PDF Setup
pdf = FPDF("P","mm","A4")
width = 210
height = 297
pdf.set_font("Arial","B",16) #font
pdf.add_page()


#Ishowed him
pdf.set_xy(10,40)

#######################Business And Client Name
pdf.cell(95,10, business_name, border=1)
pdf.cell(95,10,f"{client_name} ", align="R", border=1, ln=1)


#######################Client Address And Business
pdf.cell(95,10,business_address[0], border=1)
pdf.cell(95,10,"Default  ",align="R" ,border=1, ln=1)

pdf.cell(95,10,business_address[1], border=1)
pdf.cell(95,10,"Default  ",align="R" ,border=1, ln=1)
pdf.cell(190,4,"",ln=1,fill=True)
pdf.cell(190,8,"",ln=1)


#######################Titles
pdf.cell(52,15,"Item",align="C" ,border=1)
pdf.cell(34,15,"Unit Price",align="C" ,border=1)
pdf.cell(52,15,"Quantity",align="C" ,border=1)
pdf.cell(52,15,"Total",align="C" ,border=1,ln=1)
pdf.cell(190,8,"",ln=1)


#######################Items bought
for i in range(number):
    pdf.cell(52,15,client_data[f"item_{i}"]["item"], align="C", border=1)
    pdf.cell(34,15,client_data[f"item_{i}"]["unit price"], align="C" ,border=1)
    pdf.cell(52,15,client_data[f"item_{i}"]["quantity"], align="C", border=1)
    pdf.cell(52,15,client_data[f"item_{i}"]["sub total"], align="C", border=1,ln=1)



pdf.cell(190,8,"",ln=1)
pdf.cell(95,15, "TOTAL", border=1)
pdf.cell(95,15,f"{sub_sub_total} ", border=1,align="R", ln=1)
pdf.cell(190,8,"",ln=1)

###############Final Section
pdf.cell(50,10,"")
pdf.cell(95,10,f"Discount ",align="R")
pdf.cell(45,10,f"R{total_discount} ",align="R", border=1, ln=1)

pdf.cell(50,10,"")
pdf.cell(95,10,"Total Amount ",align="R")
pdf.cell(45,10,"0",align="R", border=1, ln=1)

pdf.cell(50,10,"")
pdf.cell(95,10,f"VAT (15%) ",align="R")
pdf.cell(45,10,f"R{total_vat} ",align="R", border=1, ln=1)

pdf.cell(50,10,"")
pdf.cell(95,10,"Amount Due ",align="R")
pdf.cell(45,10,f"R{net_net_total} ",align="R", border=1, ln=1)


pdf.output(f"{client_name}_invoice_00.pdf")
