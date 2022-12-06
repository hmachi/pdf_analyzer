from PyPDF2 import PdfFileWriter, PdfFileReader
import glob
import os

for file_name in glob.glob('divide/*.pdf'):
    (name, extention) = os.path.splitext(file_name)
    pdf_file_reader = PdfFileReader(file_name)
    page_nums = pdf_file_reader.getNumPages()

for num in range(page_nums):
    file_object = pdf_file_reader.getPage(num)
    pdf_file_name = name + '-' + str(num+1) + '.pdf'
    pdf_file_writer = PdfFileWriter()

    with open(pdf_file_name, 'wb') as f:
        pdf_file_writer.addPage(file_object)
        pdf_file_writer.write(f)
