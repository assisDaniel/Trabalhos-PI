from PIL import Image, ImageChops
import numpy as np

from erosao_dilatacao import binarizarImagem, aplicarErosao

def diferenca(imagem1_pil, imagem2_pil):
    img1NP = np.array(imagem1_pil)
    img2NP = np.array(imagem2_pil)

    img1NP = img1NP.astype(np.int16)
    img2NP = img2NP.astype(np.int16)

    diferencaNP = np.abs(img1NP - img2NP).astype(np.uint8)

    return Image.fromarray(diferencaNP)

def extrairContornos(caminhoImagem):
    imagem = Image.open(caminhoImagem)

    imagemBinariaPIL = binarizarImagem(imagem)

    imagemBinariaNp = np.array(imagemBinariaPIL, dtype=np.uint8)

    elementoEstruturante = np.array([[255, 255, 255],
                                       [255, 255, 255],
                                       [255, 255, 255]], dtype=np.uint8)

    imagemErodida = aplicarErosao(imagemBinariaNp, elementoEstruturante)

    imagemContorno = diferenca(imagemBinariaPIL, imagemErodida)

    imagemContorno.show()

if __name__ == "__main__":
    extrairContornos('uft.jpg')