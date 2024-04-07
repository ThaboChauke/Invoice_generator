from fpdf import FPDF



class FPDF(FPDF):

    def header(self):
        self.set_font("Helvetica","UB",27)
        self.cell(0,1,"INVOICE", align="C",border=1)
        self.set_xy(10,20)

pdf = FPDF("P","mm","A4")

width = 210
height = 297

pdf.set_font("Arial","B",16) #font


pdf.add_page()

pdf.cell(0,7,"cell 1", border=1, ln=0,align="C")
pdf.cell(60,7,"cell 2", border=1, ln=1)
pdf.cell(60,7,"cell 3", border=1, ln=1)





# pdf.add_page() #another page

pdf.output("invoice_00.pdf")