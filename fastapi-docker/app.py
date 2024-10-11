from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
from PIL import Image
from dotenv import load_dotenv
from util import img_analysis

app = FastAPI()


@app.get("/")
async def read_root():
    response = "Animal Detector"
    return {"Response": response}

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Check if the uploaded file is an image
    try:
        image = Image.open(file.file)
        image.verify()  # Ensure it's a valid image file
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Invalid image file")
    
    # Run analysis on the image
    try:
        response = img_analysis(image)
        return {"Response": response}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

