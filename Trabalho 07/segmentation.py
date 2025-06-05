from PIL import Image

img = Image.open('lord_shen.jpg')
imagem_cinza = img.convert('L')
imagem_cinza.show('grayscale-lord_shen.jpg')
largura, altura = imagem_cinza.size

def obterLimiar(imagem, largura, altura):
    contador = 0
    soma = 0
    for coluna in range(1, largura - 1):
        for linha in range(1, altura - 1):
            contador += 1
            soma += imagem.getpixel((coluna, linha))
    limiar = soma / contador
    return limiar

def segmentar(imagem, limiar, largura, altura):
    imagem_binaria = imagem
    for coluna in range(1, largura - 1):
        for linha in range(1, altura - 1):
            if (imagem.getpixel((coluna, linha)) < limiar):
                imagem_binaria.putpixel((coluna, linha), 0)
            else:
                imagem_binaria.putpixel((coluna, linha), 255)
    return imagem_binaria
                
limiar = obterLimiar(imagem_cinza, largura, altura)
imagem_binaria = segmentar(imagem_cinza, limiar, largura, altura)
imagem_binaria.show('segmented-lord_shen.jpg')