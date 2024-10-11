import pytest
from fastapi.testclient import TestClient
from PIL import Image, ImageFilter, ImageEnhance
import os
from io import BytesIO
from app import app  # Assuming your FastAPI app is in a file named `main.py`

client = TestClient(app)

# Helper function to convert image to bytes
def image_to_bytes(image):
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format="JPEG")
    img_byte_arr.seek(0)
    return img_byte_arr

# Helper function to perform the test
def run_image_test(image_name, expected_animal):
    image_path = os.path.join("images", image_name)
    with Image.open(image_path) as img:
        img_bytes = image_to_bytes(img)

    response = client.post("/upload/", files={"file": (image_name, img_bytes, "image/jpeg")})
    assert response.status_code == 200
    assert expected_animal in response.json()["Response"].lower()

# Test with multiple partial images
def test_partial_visible_images():
    test_cases = [
        ("dog_partial.jpeg", "dog"),
        ("cat_partial.jpeg", "cat")
    ]

    for image_name, expected_animal in test_cases:
        run_image_test(image_name, expected_animal)