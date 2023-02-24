# Created package files using script
from fpdf import FPDF
import pandas as pd

# PDF configurations
pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('../topics.csv')

for idx, row in df.iterrows():
	pdf.add_page()

	# Font configurations
	pdf.set_font(family='Times', style='B', size=24)
	pdf.set_text_color(100, 100, 100)

	pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)

	# x1 y1 x2 y2
	pdf.line(10, 21, 200, 21)

	# Iterate pages for each topic
	for i in range(row['Pages'] - 1):
		pdf.add_page()


pdf.output('output.pdf')
