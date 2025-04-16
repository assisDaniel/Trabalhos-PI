from operacaoAritmetica import OperacaoAritmetica
from operacaoGeometrica import Reflexao

# from skimage.io import imread, imshow
from PIL import Image


def main():
    img = Image.open("./Trabalho 03/imagem1.png")
    img = img.convert("L")

    op_geometrica = Reflexao(img)
    img_refletida = op_geometrica.reflexaoVertical()

    img_refletida = Image.fromarray(img_refletida)
    img_refletida.save("./Trabalho 03/resultado-reflexao-v.png")

    op_geometrica = Reflexao(img)
    img_refletida = op_geometrica.reflexaoHorizontal()

    img_refletida = Image.fromarray(img_refletida)
    img_refletida.save("./Trabalho 03/resultado-reflexao-h.png")

    img_2 = Image.open("./Trabalho 03/imagem1.png")
    img_2 = img_2.convert("L")

    op_aritmetica = OperacaoAritmetica(imagem_1=img, imagem_2=img_2)
    soma, subtracao = op_aritmetica.operacaoAritmetica()

    soma = Image.fromarray(soma)
    soma.save("./Trabalho 03/Resultados/resultado-soma.png")

    subtracao = Image.fromarray(subtracao)
    subtracao.save("./Trabalho 03/Resultados/resultado-subtracao.png")

if __name__ == "__main__":
    main()