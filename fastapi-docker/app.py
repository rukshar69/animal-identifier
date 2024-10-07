from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv


# Load environment variables from .env file
# load_dotenv()

# Access the API_KEY environment variable
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

app = FastAPI()

def img_analysis(image):
    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction="You are an expert animal identifier. Given an image of an animal, tell me the name of the animal in the image."\
        "If the image is not an animal, output 'not animal'. Otherwise, output the name of the animal only. Do not output any other text or symbols or newline.",
    )
    response = model.generate_content([image, "What is the name of the animal in the image?"])
    return response.text


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
