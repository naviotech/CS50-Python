from fpdf import FPDF
class Shirt:
    def __init__(self, name = None):
        self.name = name
        self.stamping()

    @classmethod
    def get_name(cls):
        name = input("Write your full name: ").strip()
        return cls(name)
    
    def stamping(self):
        pdf = FPDF(orientation="Portrait", format="A4")
        pdf.add_page()
        pdf.set_font('helvetica', 'B', 40)
        pdf.set_text_color(107,25,55)
        pdf.cell(0, 80, 'CS50 Shirtificate', align='C')
        pdf.ln()
        
        pdf.image("shirtificate.png",x=15,y=(297 / 4), w=180, alt_text= f"{self.name} took CS50")
        pdf.set_font("helvetica", "B", size=20)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 80, border=0, align="C", txt=f"{self.name} took CS50")
        pdf.output("shirtificate.pdf")


def main():
   Shirt.get_name()
    
if __name__ == "__main__":
    main()