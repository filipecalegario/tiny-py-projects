# pdf_splitting.py

from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

def split(input_pdf_name, from_page, to_page, output_pdf_name):
    pdf = PdfFileReader(input_pdf_name)
    pdf_writer = PdfFileWriter()
    for page_number in range(from_page-1,to_page):
        pdf_writer.addPage(pdf.getPage(page_number))

    output = f'{output_pdf_name}.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]
    pages_in = int(sys.argv[3])
    pages_out = int(sys.argv[4])
    print(sys.argv)
    split(input, pages_in, pages_out, output)
    #filename = '/Users/fcac/Dropbox/DOUTORADO/MTL REFS/AFTER DEFENSE/10.1007@978-3-030-43859-3.pdf'
    # split(filename, 59, 79, filename+'_ch03')
    # split(filename, 80, 98, filename+'_ch04')
    # split(filename, 99, 127, filename+'_ch05')
    # split(filename, 128, 146, filename+'_ch06')
    # split(filename, 147, 164, filename+'_ch07')
    # split(filename, 165, 200, filename+'_ch08')
    # split(filename, 201, 215, filename+'_ch09')
    # split(filename, 216, 241, filename+'_ch10')
    # split(filename, 242, 259, filename+'_ch11')
    # split(filename, 260, 279, filename+'_ch12')
    # split(filename, 280, 309, filename+'_ch13')
    # split(filename, 310, 331, filename+'_ch14')
    # split(filename, 332, 357, filename+'_ch15')
    # split(filename, 358, 403, filename+'_ch16')
    #split(filename, 513 , 517, filename.split('.')[0]+'_compcrea')
    #split(filename, 23 , 27, '/Users/fcac/Dropbox/SERRAPILHEIRA 2019/Refs/DIRETO/DEEP LEARNING AND CO-CREATIVITY/'+'White2019')
    #split(filename, 29, 46, '/Users/fcac/Dropbox/DOUTORADO/MTL REFS/AFTER DEFENSE/Colton2020.pdf')
    