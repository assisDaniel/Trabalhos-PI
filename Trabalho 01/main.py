from interpolacaoVizinho import InterpolacaoVizinho
from interpolacaoBilinear import InterpolacaoBilinear

def main():
    choice = input("Digite 1 para vizinho mais próximo e 2 para bilinear:")

    if choice == '1':
        arquivo_matriz = './Trabalho 01/imagem1.png'
        interpolador = InterpolacaoVizinho(arquivo_matriz)
        matrizes_reduzidas, matrizes_ampliadas = interpolador.processar_imagens()
        interpolador.salvar_imagens(matrizes_reduzidas, matrizes_ampliadas)
        interpolador.mostrar_resultados(matrizes_reduzidas, matrizes_ampliadas)
    else:
        caminho_imagem = '/home/assisdaniel/Documentos/UFT/6º Período/Processamento de Imagens/Implementações/Trabalho 01/imagem1.png'
        interpolador = InterpolacaoBilinear(caminho_imagem)
        matrizes_reduzidas, matrizes_ampliadas = interpolador.processar_imagens()
        interpolador.salvar_imagens(matrizes_reduzidas, matrizes_ampliadas, prefixo_saida='resultado_bilinear')
        interpolador.mostrar_resultados(matrizes_reduzidas, matrizes_ampliadas)


if __name__ == "__main__":
    main()