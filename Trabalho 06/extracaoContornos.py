from PIL import Image, ImageChops
import numpy as np

from erosao_dilatacao import binarizarImagem, aplicarErosao

def extrairContornos(caminhoImagem):
    imagem = Image.open(caminhoImagem)

    imagemBinariaPIL = binarizarImagem(imagem)

    imagemBinariaNp = np.array(imagemBinariaPIL, dtype=np.uint8)

    elementoEstruturante = np.array([[255, 255, 255],
                                       [255, 255, 255],
                                       [255, 255, 255]], dtype=np.uint8)

    imagemErodida = aplicarErosao(imagemBinariaNp, elementoEstruturante)

    imagemContorno = ImageChops.difference(imagemBinariaPIL, imagemErodida)

    imagemContorno.show()

if __name__ == "__main__":
    extrairContornos('uft.jpg')