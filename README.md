# animal-identifier
Identify animals using multimodal Gemini API

# Backend

We have FastAPI backend with one API */upload* which accepts an image and returns the name of the animal in the image. The API uses Gemini API to generate animal names through multimodal prompt engineering. The model used here is gemini-1.5-flash.

Some tests are performed on the API. The details of the tests are included in a separate [README file](https://github.com/rukshar69/animal-identifier/blob/main/fastapi-docker/test_doc/test.md).
