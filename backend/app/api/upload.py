from pathlib import Path

from fastapi import APIRouter, UploadFile, File

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

    return {
        "filename": file.filename,
        "saved_to": str(destination)
    }