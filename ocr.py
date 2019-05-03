from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pattern='ZEA[0-9]+'
def ocr_core(filename):  
    
    text = pytesseract.image_to_string(Image.open(filename))  
    return text
id=[]
img = 'scan2.png'



val=ocr_core(img)
val=val.replace('—','')
    # id.append(re.findall(pattern,val))
print(val)

# print(id)

