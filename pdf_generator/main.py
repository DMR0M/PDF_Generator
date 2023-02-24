# Created package files using script
from fpdf import FPDF
import pandas as pd
from pathlib import Path

# Generating PDF in Python
# PDF configurations
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv(Path.cwd().parent / 'topics.csv')


def add_lines(boundary=31) -> None:
	for n in range(25):
		pdf.line(10, boundary, 200, boundary)
		boundary += 10


def main():
	for idx, row in df.iterrows():
		pdf.add_page()

		# Set Header
		# Font configurations
		pdf.set_font(family='Times', style='B', size=24)
		pdf.set_text_color(100, 100, 100)

		# Create a pdf cell
		pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)

		# x1 y1 x2 y2
		pdf.line(10, 21, 200, 21)

		# add lines function
		add_lines()

		# ln adds empty break lines
		pdf.ln(260)

		# Set Footer
		pdf.set_font(family='Times', style='I', size=10)
		pdf.set_text_color(180, 180, 180)
		pdf.cell(w=0, h=12, txt=row['Topic'], align='R', ln=1)

		# Iterate pages for each topic
		for i in range(row['Pages'] - 1):
			pdf.add_page()
			add_lines()
			# Add Footer
			pdf.ln(270)
			pdf.set_font(family='Times', style='I', size=10)
			pdf.set_text_color(180, 180, 180)
			pdf.cell(w=0, h=12, txt=row['Topic'], align='R', ln=1)

	# Create the pdf file
	pdf.output('output.pdf')


if __name__ == '__main__':
	main()
