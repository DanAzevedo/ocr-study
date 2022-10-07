import cv2
import pytesseract as pt

# Extrair char por char da imagem com a localização exata

pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('imgtest.jpg')
# Não precisa converter para escala de cinza pois a imagem já está binária
boxes = pt.pytesseract.image_to_boxes(img)
imH, imW, _ = img.shape
'''
- Percorremos todas as informações, porém, dividimos elas em linhas splitlines() e extrair os dados.
- Pegamos a informação da linha e dividimos em espaço obtendo todos os valores correspondente a localização.
  Separamos por "espaço", criamos uma array e alocamos cada uma dessas informações no mesmo.  
'''
for b in boxes.splitlines():
    b = b.split(' ')
    letra, x, y, w, h = b[0], int(b[1]), int(b[2]), int(b[3]), int(b[4])
    # Não sei por qual motivo, mas para chegar exatamento no valor de Y, precisamos subtrair a imH da imagem original de Y
    cv2.rectangle(img, (x, imH - y), (w, imH - h), (0, 0, 255), 1)
    cv2.putText(img, letra, (x, imH - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)
