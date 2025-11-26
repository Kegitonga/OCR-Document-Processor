"""ocr.py - demo using pytesseract
pip install pytesseract pillow
Requires tesseract installed on the system.
"""
from PIL import Image
import pytesseract
import sys

def ocr_image(path):
    img = Image.open(path)
    return pytesseract.image_to_string(img)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python ocr.py /path/to/image.png')
    else:
        print(ocr_image(sys.argv[1]))
