# Functional Testing

## Valid Image Input:

Test with 5 valid animal images(dog, iguana, lion, tiger, and wolf) to ensure the API correctly identifies the animal names.

## Non-Animal Image Input:

Test API with images without animals (chair and pillow) to verify that the output is **not animal**.

# Image Quality:

- Test with low-resolution images to determine if the AI can still accurately classify them.
- Use images that are too dark or blurred and verify if the model struggles to make an identification.

# Error and Edge Case Tests

## Invalid Input Types:

- Pass non-image data (e.g., text) to see if it correctly raises an error 
- Test with corrupt images or unsupported file types(txt file) to ensure it returns correct error handling messages.

# Boundary Cases:

- Provide images with partially visible animals( partially visible cat or dog) and check the response produces correct animal name. **I had to change the prompt becuase the dog image was returning the breed name but I only wanted the animal name.**

