import fitz
from docx import Document
import os


def extract_text(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf(file_path)

    elif extension == ".docx":
        return extract_docx(file_path)

    raise Exception("Unsupported file format")


def extract_pdf(file_path):
    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text


def extract_docx(file_path):
    document = Document(file_path)

    return "\n".join(paragraph.text for paragraph in document.paragraphs)