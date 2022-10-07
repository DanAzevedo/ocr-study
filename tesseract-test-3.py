import cv2
import pytesseract as pt

# Extrair char por char da imagem com a localização exata

pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('imgtest.jpg')
# Não precisa converter para escala de cinza pois a imagem já está binária
data = pt.pytesseract.image_to_data(img)
imH, imW, _ = img.shape

'''
Percorremos e colocamos on índice em cada linha splitline() da variável data.
Fazemos isso pelo fato de na primeira linha termos o cabeçalho, e não precisamos dessa informação.
'''
for x, lines in enumerate(data.splitlines()):
    # Excluimos a linha 0 que onde está o cabeçalho
    if x != 0:
        # Nessa métrica, filtramos apenas linhas que contém uma palavra ao final
        # Um array qye retornar com 12 posições, tem uma palavra no final, com 11, não
        lines = lines.split()
        # print(lines)
        if len(lines) == 12:
            # Variáveis abaixo estão nas posições 6, 7, 8, e 9
            x, y, w, h = int(lines[6]), int(lines[7]), int(lines[8]), int(lines[9])
            word = lines[11]
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
            cv2.putText(img, word, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)
