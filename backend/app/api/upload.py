from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from app.services.parser_service import extract_resume_text

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/")
async def upload_resume(file: UploadFile = File(...)):
    destination = UPLOAD_DIR / file.filename

    with open(destination, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_resume_text(str(destination))

    return {
        "filename": file.filename,
        "text": text
    }