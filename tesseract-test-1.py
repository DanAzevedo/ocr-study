import cv2
import pytesseract as pt

pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('imgtest.jpg')
# Não precisa converter para escala de cinza pois a imagem já está binária
print(pt.pytesseract.image_to_string(img, lang='por'))

cv2.imshow('Image', img)
cv2.waitKey(0)