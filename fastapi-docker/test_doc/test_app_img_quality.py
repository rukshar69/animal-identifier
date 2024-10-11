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

# Test with a low-resolution version of the image
def test_low_resolution_image():
    image_path = os.path.join("images", "dog.jpg")
    with Image.open(image_path) as img:
        # Resize the image to low resolution (e.g., 20x20)
        low_res_image = img.resize((20, 20))
        img_bytes = image_to_bytes(low_res_image)

    response = client.post("/upload/", files={"file": ("low_res_dog.jpg", img_bytes, "image/jpeg")})
    assert response.status_code == 200
    assert "dog" in response.json()["Response"].lower()

# Test with a blurred version of the image
def test_blurred_image():
    image_path = os.path.join("images", "wolf.jpeg")
    with Image.open(image_path) as img:
        # Apply blur filter
        blurred_image = img.filter(ImageFilter.GaussianBlur(radius=5))
        img_bytes = image_to_bytes(blurred_image)

    response = client.post("/upload/", files={"file": ("blurred_wolf.jpg", img_bytes, "image/jpeg")})
    assert response.status_code == 200
    assert "wolf" in response.json()["Response"].lower()

# Test with a dark version of the image
def test_dark_image():
    image_path = os.path.join("images", "Iguana.jpg")
    with Image.open(image_path) as img:
        # Darken the image
        enhancer = ImageEnhance.Brightness(img)
        dark_image = enhancer.enhance(0.2)  # Adjust brightness to 20%
        img_bytes = image_to_bytes(dark_image)

    response = client.post("/upload/", files={"file": ("dark_iguana.jpg", img_bytes, "image/jpeg")})
    assert response.status_code == 200
    assert "iguana" in response.json()["Response"].lower()

# Test with a correctly sized image (control case)
def test_normal_image():
    image_path = os.path.join("images", "lion.jpg")
    with Image.open(image_path) as img:
        img_bytes = image_to_bytes(img)

    response = client.post("/upload/", files={"file": ("lion.jpg", img_bytes, "image/jpeg")})
    assert response.status_code == 200
    assert "lion" in response.json()["Response"].lower()
