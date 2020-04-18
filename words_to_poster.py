from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import mm

font_size = 10
main_font = 'Helvetica'
main_font_bold = main_font + '-Bold'


words = open('input.txt').read().split('\n')
c = canvas.Canvas("output.pdf", bottomup=0, pagesize=landscape(A4))
height, width = A4
margin_horizontal = 10*mm
margin_vertical = 10*mm
width = width - margin_horizontal*2
height = height - margin_vertical*2

pointer_x = margin_horizontal
pointer_y = margin_vertical


