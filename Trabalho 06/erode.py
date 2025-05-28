from PIL import Image
import numpy as np

def binarizarImagem(imagem, limiar=128):
    """Converte a imagem para binário."""
    return imagem.convert('L').point(lambda p: 255 if p > limiar else 0, mode='1')

def erosao(imagem_np, nucleo):
    imagem_erodida = imagem_np.copy()
    linhas, colunas = imagem_np.shape
    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            valor = np.uint8(255)
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if imagem_np[i + k, j + l] != nucleo[k + 1, l + 1]:
                        valor = np.uint8(0)
                        break
                if valor == 0:
                    break
            imagem_erodida[i, j] = valor
    return Image.fromarray(imagem_erodida)

imagem = Image.open('uft.jpg')
imagem_binaria = binarizarImagem(imagem).convert('L')

imagem_binaria_np = np.array(imagem_binaria, dtype=np.uint8)

nucleo = np.array([[255, 255, 255],
                   [255, 255, 255],
                   [255, 255, 255]], dtype=np.uint8)

imagem_erodida = erosao(imagem_binaria_np, nucleo)

imagem_erodida.show('uft.jpg')
