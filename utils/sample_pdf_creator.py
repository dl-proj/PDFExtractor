from PyPDF2 import PdfFileReader, PdfFileWriter
from pdfreader import SimplePDFViewer
from pdfrw import PdfReader, PdfWriter


def create_sample_pdf(pdf_path):
    fd = open(pdf_path, "rb")
    reader_viewer = SimplePDFViewer(fd)
    reader_viewer.render()
    markdown = reader_viewer.canvas.text_content
    pdf_str = reader_viewer.canvas.strings

    rw_viewer = PdfReader(pdf_path)
    rw_content = rw_viewer.pages[0].Contents.stream
    pdf = PdfFileReader(pdf_path)
    pdf_writer = PdfFileWriter()
    report_page = pdf.getPage(0)
    report_page.extractText()

    return


if __name__ == '__main__':

    create_sample_pdf(pdf_path="")
