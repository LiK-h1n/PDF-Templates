from fpdf import FPDF
from pandas import read_csv


def set_footer(lines):
    pdf.ln(lines)
    pdf.set_font("Times", "I", 8)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, row["Topic"], 0, 1, "R")


def create_lines(header=True):
    if header:
        y1, y2 = 31, 31
        num_of_lines = 26
    else:
        y1, y2 = 21, 21
        num_of_lines = 27

    for i in range(num_of_lines):
        pdf.line(10, y1, 200, y2)
        y1 += 10
        y2 += 10


pdf = FPDF("P", "mm", "A4")
pdf.set_auto_page_break(False, 0)

df = read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Times", "B", 24)
    pdf.cell(0, 12, row["Topic"], 0, 1, "L")
    pdf.line(10, 21, 200, 21)
    set_footer(265)
    create_lines()

    for i in range(int(row["Pages"] - 1)):
        pdf.add_page()
        set_footer(277)
        create_lines(False)

pdf.output("output.pdf")
