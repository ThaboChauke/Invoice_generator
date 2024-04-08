from fpdf import FPDF
# from user_input import company_details,collect_info


# client,data_list = collect_info()

class FPDF(FPDF):

    def header(self):
        self.set_font("Helvetica","UB",27)
        self.cell(0,15,"INVOICE", align="C",border=1)
        self.set_xy(10,20)

    def footer(self) -> None:
        self.set_font("Helvetica", "B",10)
        self.set_xy(10,287)
        self.cell(0,7, "011-012-3654/kingconstruction@co.business.co.za", align="C")

pdf = FPDF("P","mm","A4")

width = 210
height = 297

pdf.set_font("Arial","B",16) #font


pdf.add_page()

pdf.set_xy(10,40)
pdf.cell(95,40, "Cell 1", border=1)

#Ishowed him
pdf.cell(95,40,"cell 2  ",align="R" ,border=1, ln=1)
pdf.cell(190,8,"",ln=1)

for i in range(5):
    pdf.cell(63.33,15,"cell 4", border=1)
    pdf.cell(63.33,15,"cell 5", border=1)
    pdf.cell(63.33,15,"cell 6", border=1,ln=1)

pdf.cell(190,8,"",ln=1)
pdf.cell(95,15, "TOTAL", border=1)
pdf.cell(95,15,"cell 2  ", border=1,align="R", ln=1)
pdf.cell(190,8,"",ln=1)
pdf.cell(95,40,"",)
pdf.cell(95,40,"cell 2", border=1)


# pdf.add_page() #another page

pdf.output("invoice_00.pdf")