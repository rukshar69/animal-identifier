import pytest
from fastapi.testclient import TestClient
from io import BytesIO
from PIL import Image
from app import app  # Assuming the FastAPI app is defined in main.py

client = TestClient(app)

# Helper function to create a fake image
def create_image():
    image = Image.new("RGB", (100, 100), color="red")
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

# Helper function to create corrupted image
def create_corrupted_image():
    corrupted_data = b"thisisnotanimage"
    return BytesIO(corrupted_data)

# Test: Passing non-image data (e.g., text, numbers)
def test_non_image_data():
    files = {'file': ('text_file.txt', BytesIO(b"This is some text data"), 'text/plain')}
    response = client.post("/upload/", files=files)
    assert response.status_code == 400
    assert "cannot identify image file" in response.json()["error"]

# Test: Passing corrupted image
def test_corrupted_image():
    files = {'file': ('corrupted_image.png', create_corrupted_image(), 'image/png')}
    response = client.post("/upload/", files=files)
    assert response.status_code == 400
    assert "cannot identify image file" in response.json()["error"]

# Test: Unsupported file types
def test_unsupported_file_type():
    files = {'file': ('text_file.txt', BytesIO(b"12345"), 'text/plain')}
    response = client.post("/upload/", files=files)
    assert response.status_code == 400
    assert "cannot identify image file" in response.json()["error"]

# Test: Passing valid image
def test_valid_image():
    files = {'file': ('test_image.png', create_image(), 'image/png')}
    response = client.post("/upload/", files=files)
    assert response.status_code == 200
    assert "Response" in response.json()
