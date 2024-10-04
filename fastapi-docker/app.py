# create a fastapi get api that will return a json containing a string hello world

from fastapi import FastAPI
import google.generativeai as genai #https://ai.google.dev/pricing
from dotenv import load_dotenv
import os
import PIL.Image


# Load environment variables from .env file
load_dotenv()

# Access the API_KEY environment variable
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

app = FastAPI()

def img_analysis():
    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction="You are expert animal identifier. Given an image of"\
            "an animal, tell me the name of the animal in the image",)
    animal_img = PIL.Image.open( "images/tiger.jpg")
    response = model.generate_content([animal_img, "What is the name of the animal in the image?"], max_tokens=10)
    print(response)
    return response.text


@app.get("/")
async def read_root():
    response = img_analysis()
    return {"Response": response}