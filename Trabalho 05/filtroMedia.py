from PIL import Image
import numpy as np

"""
Máscara do Filtro

1   1   1
1   1   1
1   1   1

Logo, o multiplicador constante é 1/9 
"""

try:
    imagem = np.array(Image.open("Trabalho 05/lena.png").convert("L"))
except FileNotFoundError:
    print("Imagem não encontrada. Verifique o nome do arquivo.")
    exit()

linhas, colunas = imagem.shape  
print('Linhas:', linhas, 'Colunas:', colunas)

mascara = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
divConstante = sum(sum(linha) for linha in mascara) 
print(divConstante)

novaMatriz = np.zeros((linhas, colunas), dtype=np.uint8)  

def pegarValorMatriz(linha, coluna):
    if 0 <= linha < linhas and 0 <= coluna < colunas:
        return int(imagem[linha, coluna])
    return 0

for i in range(linhas):
    for j in range(colunas):
        valor = (
            mascara[0][0] * pegarValorMatriz(i-1, j-1) +
            mascara[0][1] * pegarValorMatriz(i-1, j)   +
            mascara[0][2] * pegarValorMatriz(i-1, j+1) +
            mascara[1][0] * pegarValorMatriz(i, j-1)   +
            mascara[1][1] * pegarValorMatriz(i, j)     +
            mascara[1][2] * pegarValorMatriz(i, j+1)   +
            mascara[2][0] * pegarValorMatriz(i+1, j-1) +
            mascara[2][1] * pegarValorMatriz(i+1, j)   +
            mascara[2][2] * pegarValorMatriz(i+1, j+1)
        ) // divConstante
        
        novaMatriz[i, j] = np.clip(valor, 0, 255)

novaImagem = Image.fromarray(novaMatriz)
# novaImagem.save("resultado.png")
novaImagem.show()