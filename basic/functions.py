import os

import PyPDF2
#%%

class ConvertPage:
    original = "file_to_ocr.pdf"
    target = "output.pdf"
    temp_txt = 'output.txt'

    def __init__(self, file):
        self.file = file
        self.process_file()

    def process_file(self):
        left, right, top, bottom = (300, 800, 950, 200)
        pdf = PyPDF2.PdfFileReader(self.file)
        out = PyPDF2.PdfFileWriter()

        page = pdf.getPage(0)
        print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())

        page.mediaBox.upperRight = (top, right)
        page.mediaBox.lowerLeft = (bottom, left)
        # page.mediaBox.lowerRight = (right, bottom)
        # page.mediaBox.upperLeft = (left, top)
        out.addPage(page)
        ous = open(self.target, 'wb')
        out.write(ous)
        ous.close()

    def get_result(self):
        os.system(f'pdftotext {self.target} {self.temp_txt}')
        with open(self.temp_txt, 'r') as stream:
            output = stream.read()
        return output

'''
def convert_page(file):
    # file = open(original, 'rb')
    left,right,top,bottom = (300,800,950,200)
    pdf = PyPDF2.PdfFileReader(file)
    out = PyPDF2.PdfFileWriter()

    page = pdf.getPage(0)
    print (page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())




    page.mediaBox.upperRight = (top, right)
    page.mediaBox.lowerLeft  = (bottom, left)
    # page.mediaBox.lowerRight = (right, bottom)
    # page.mediaBox.upperLeft = (left, top)
    out.addPage(page)
    ous = open(target, 'wb')
    out.write(ous)
    ous.close()
    os.system(f'pdftotext {target} {temp_txt}')
    with open(temp_txt,'r') as stream:
        output = stream.read()
    return output
'''
 #%%



