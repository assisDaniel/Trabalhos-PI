from PIL import Image
import numpy as np

def binarizarImagem(imagem, limiar=128):
    """Converte a imagem para binário."""
    return imagem.convert('L').point(lambda p: 255 if p > limiar else 0, mode='1')

def dilatar(imagem, nucleo):
    imagem = np.array(imagem, dtype=np.uint8)
    imagem_dilatada = imagem.copy()
    linhas, colunas = imagem.shape
    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            comparar = False
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if imagem[i+k, j+l] == nucleo[k+1, l+1]:
                        comparar = True
                        break
                if comparar:
                    break
            imagem_dilatada[i, j] = 255 if comparar else 0
    return Image.fromarray(imagem_dilatada)

imagem = Image.open('placa.jpg')

imagem_binaria = binarizarImagem(imagem)

imagem_binaria.save('placa-binarizada.jpg')

imagem_binaria_np = np.array(imagem_binaria, dtype=np.uint8)

nucleo = np.array([[255, 255, 255],
                   [255, 255, 255],
                   [255, 255, 255]], dtype=np.uint8)

imagem_dilatada = dilatar(imagem_binaria_np, nucleo)

imagem_dilatada.save('placa-dilatada.jpg')
