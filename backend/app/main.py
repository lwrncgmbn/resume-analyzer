from fastapi import FastAPI
from app.api.upload import router as upload_router

from app.api.analyze import router as analyze_router


app = FastAPI(
    title="Resume Analyzer API",
    version="1.0.0"
)

app.include_router(upload_router)

app.include_router(analyze_router)

@app.get("/")
async def root():
    return {
        "message": "Resume Analyzer API is running!"
    }