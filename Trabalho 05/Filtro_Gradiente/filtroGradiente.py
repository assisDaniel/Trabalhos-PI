from PIL import Image
import numpy as np

try:
    imagem = np.array(Image.open("lena.png").convert("L"))
except FileNotFoundError:
    print("Imagem não encontrada. Verifique o nome do arquivo.")
    exit()

linhas, colunas = imagem.shape  
print('Linhas:', linhas, 'Colunas:', colunas)

novaMatriz = np.zeros((linhas, colunas), dtype=np.uint8)

filtroSobelX = [[-1, -2, -1],
                  [ 0,  0,  0],
                  [ 1,  2,  1]]

filtroSobelY = [[-1, 0, 1],
                  [-2, 0, 2],
                  [-1, 0, 1]]

def pegarValorMatriz(linha, coluna):
    if 0 <= linha < linhas and 0 <= coluna < colunas:
        return int(imagem[linha, coluna])
    return 0

for i in range(1, linhas - 1):
    for j in range(1, colunas - 1):
        gx = 0
        gy = 0

        for k in range(3):
            for l in range(3):
                valorPixel = pegarValorMatriz(i + k - 1, j + l - 1)
                gx += valorPixel * filtroSobelX[k][l]
                gy += valorPixel * filtroSobelY[k][l]
        
        magnitude = int(np.sqrt(gx**2 + gy**2))

        if magnitude > 255:
            magnitude = 255

        novaMatriz[i, j] = magnitude

resultado = Image.fromarray(novaMatriz)
resultado.show()

# resultado.save("lena_sobel.png")
