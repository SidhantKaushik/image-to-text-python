import pytesseract
import cv2
import re
from googletrans import Translator
p = Translator()

imageInput = input("Please enter an image file location: ")
language = input("Please enter the language you would like to translate to: ")

img = cv2.imread(imageInput)
out = pytesseract.image_to_string(img)
trans = str(p.translate(out, dest=language))

m = trans.find("text")
position2 = (trans.find("pr"))
m = m + 5
position2 = position2 - 2

print(out)
print(trans[m:position2])