
import pandas as pd
from fpdf import FPDF
from datetime import datetime

# Read CSV data
df = pd.read_csv("internship_completion_list.csv")

# PDF Report Class
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "CODTECH Internship Completion Certificates", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}", align="C")

    def add_certificate(self, name, dept, date):
        self.add_page()
        self.set_font("Arial", "B", 16)
        self.ln(40)
        self.cell(0, 10, "INTERNSHIP COMPLETION CERTIFICATE", ln=True, align="C")
        self.ln(10)
        self.set_font("Arial", "", 12)
        text = f"This is to certify that {name} has successfully completed their internship in the {dept} department at CODTECH."
        self.multi_cell(0, 10, text, align="C")
        self.ln(10)
        self.cell(0, 10, f"Issued on: {date}", ln=True, align="C")
        self.ln(20)
        self.cell(0, 10, "Automated Report Generator", ln=True, align="C")

# Generate PDF
pdf = PDFReport()

for index, row in df.iterrows():
    pdf.add_certificate(row['Name'], row['Internship Department'], row['Completion Date'])

pdf.output("sample_report.pdf")
print("PDF Report Generated: sample_report.pdf")