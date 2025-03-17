from PIL import Image

def encode_image(image_path, secret_text):
    img = Image.open(image_path)
    encoded = img.copy()
    pixels = encoded.load()

    for i in range(len(secret_text)):
        pixels[i, 0] = (pixels[i, 0][0], pixels[i, 0][1], ord(secret_text[i]))

    encoded.save("encoded_image.png")

encode_image("input.png", "Hidden Message")
print("Image encoded successfully!")
