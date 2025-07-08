import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os
import cv2
import numpy as np

# Optional: Point to your tesseract installation (if not in PATH)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(pil_image):
    # Convert PIL image to OpenCV image
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # Convert back to PIL for pytesseract
    return Image.fromarray(thresh)

def extract_text_from_file(filepath):
    text = ""
    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".pdf":
        images = convert_from_path(filepath)
        for image in images:
            image = preprocess_image(image)
            text += pytesseract.image_to_string(image, config='--psm 6')
    elif ext in [".png", ".jpg", ".jpeg", ".bmp"]:
        image = preprocess_image(Image.open(filepath))
        text = pytesseract.image_to_string(image, config='--psm 6')
    else:
        raise ValueError("Unsupported file type")

    return text
