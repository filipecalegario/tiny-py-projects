# pdf_splitting.py

from PyPDF2 import PdfFileReader, PdfFileWriter

def split(input_pdf_name, from_page, to_page, output_pdf_name):
    pdf = PdfFileReader(input_pdf_name)
    pdf_writer = PdfFileWriter()
    for page_number in range(from_page-1,to_page):
        pdf_writer.addPage(pdf.getPage(page_number))

    output = f'{output_pdf_name}.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

if __name__ == '__main__':
    split('/Users/fcac/Dropbox/DOUTORADO/MTL REFS/AFTER DEFENSE/10.1007@978-3-030-33617-2.pdf',
          51,
          62,
          '/Users/fcac/Dropbox/DOUTORADO/MTL REFS/AFTER DEFENSE/10.1007@978-3-030-33617-2_selected.pdf')