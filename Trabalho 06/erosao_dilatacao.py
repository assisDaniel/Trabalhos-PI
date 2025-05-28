from PIL import Image
import numpy as np

def binarizarImagem(imagem, limiar=128):
    return imagem.convert('L').point(lambda p: 255 if p > limiar else 0)

def aplicarErosao(imagemNp, elementoEstruturante):
    imagemErodida = imagemNp.copy()
    linhas, colunas = imagemNp.shape
    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            valor = 255
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if imagemNp[i + k, j + l] != elementoEstruturante[k + 1, l + 1]:
                        valor = 0
                        break
                if valor == 0:
                    break
            imagemErodida[i, j] = valor
    return Image.fromarray(imagemErodida)

def aplicarDilatacao(imagemNp, elementoEstruturante):
    """Expande as áreas brancas."""
    imagemDilatada = imagemNp.copy()
    linhas, colunas = imagemNp.shape
    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            valor = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if imagemNp[i + k, j + l] == 255 and elementoEstruturante[k + 1, l + 1] == 255:
                        valor = 255
                        break
                if valor == 255:
                    break
            imagemDilatada[i, j] = valor
    return Image.fromarray(imagemDilatada)

if __name__ == "__main__":
    imagem = Image.open('uft.jpg')

    imagemBinaria = np.array(binarizarImagem(imagem), dtype=np.uint8)

    elementoEstruturante = np.array([[255, 255, 255],
                    [255, 255, 255],
                    [255, 255, 255]], dtype=np.uint8)

    imagemErodida = aplicarErosao(imagemBinaria, elementoEstruturante)
    imagemDilatada = aplicarDilatacao(imagemBinaria, elementoEstruturante)

    imagemErodida.show()
    imagemDilatada.show()