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
    try:
        image = Image.open(file.file)
        response = img_analysis(image)
        return {"Response": response}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
