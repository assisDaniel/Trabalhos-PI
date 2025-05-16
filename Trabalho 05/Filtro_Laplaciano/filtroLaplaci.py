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

# Filtros Laplacianos
primeirofiltro = [[0,1,0],[1,-4,1],[0,1,0]]
segundofiltro  = [[0,-1,0],[-1,4,-1],[0,-1,0]]
terceirofiltro = [[1,1,1],[1,-8,1],[1,1,1]]
quartofiltro   = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]

def pegarValorMatriz(linha, coluna):
    if 0 <= linha < linhas and 0 <= coluna < colunas:
        return int(imagem[linha, coluna])
    return 0

while True:
    print("\nEscolha qual filtro Laplaciano aplicar:")
    print("1 - Primeiro Filtro (0,1,0 / 1,-4,1 / 0,1,0)")
    print("2 - Segundo Filtro (0,-1,0 / -1,4,-1 / 0,-1,0)")
    print("3 - Terceiro Filtro (1,1,1 / 1,-8,1 / 1,1,1)")
    print("4 - Quarto Filtro (-1,-1,-1 / -1,8,-1 / -1,-1,-1)")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '0':
        print("Saindo.")
        break
    elif opcao == '1':
        filtro = primeirofiltro
        nome_filtro = "filtro1"
    elif opcao == '2':
        filtro = segundofiltro
        nome_filtro = "filtro2"
    elif opcao == '3':
        filtro = terceirofiltro
        nome_filtro = "filtro3"
    elif opcao == '4':
        filtro = quartofiltro
        nome_filtro = "filtro4"
    else:
        print("Opção inválida. Tente novamente.")
        continue

    # Aplica o filtro Laplaciano
    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            valor = 0

            for k in range(3):
                for l in range(3):
                    valor += pegarValorMatriz(i + k - 1, j + l - 1) * filtro[k][l]
            
            if valor < 0:
                valor = 0
            elif valor > 255:
                valor = 255
            novaMatriz[i, j] = valor

    resultado = Image.fromarray(novaMatriz)
    caminho_saida = f"/home/tarcisof/Documentos/Trabalhos-PI/Trabalho 05/Filtro_Laplaciano/lena.png"
    resultado.save(caminho_saida)
