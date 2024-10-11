import google.generativeai as genai
import os

def img_analysis(image):
    api_key = os.getenv("API_KEY")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction="You are an expert animal identifier. Given an image of an animal, tell me the name of the animal in the image."\
        "Do not output what breed of animal the image is."\
        "If the image is not an animal, output 'not animal'. Otherwise, output the name of the animal only. Do not output any other text or symbols or newline.",
    )
    try:
        response = model.generate_content([image, "What is the name of the animal in the image?"])
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing image.")
