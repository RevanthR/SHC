import Image
from tesseract import image_to_string
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
print image_to_string(Image.open('scan2.png'))
