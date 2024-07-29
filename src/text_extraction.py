import PyPDF2
from tika import parser


def extract_text_pypdf2(pdf_path):
    """
    Extracts text from a PDF file using PyPDF2.

    Args:
        pdf_path (str): The file path of the PDF document.

    Returns:
        str: The extracted text from the PDF document.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
        return text


def extract_text_tika(pdf_path):
    """
    Extracts text from a PDF file using Tika.

    Args:
        pdf_path (str): The file path of the PDF document.

    Returns:
        str: The extracted text from the PDF document.
    """
    parsed = parser.from_file(pdf_path)
    return parsed['content']
