from pathlib import Path

from app.services.pdf_service import extract_pdf_text
from app.services.docx_service import extract_docx_text


def extract_resume_text(file_path: str) -> str:
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    if extension == ".docx":
        return extract_docx_text(file_path)

    raise ValueError("Unsupported file type")