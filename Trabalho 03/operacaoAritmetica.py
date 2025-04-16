import numpy as np


class OperacaoAritmetica:
    def __init__(self, imagem_1, imagem_2):
        self.imagem_1 = np.array(imagem_1)
        self.imagem_2 = np.array(imagem_2)

    def verificarTamanhoSoma(self, matriz_verificada):
        """Verificar matriz para valores maiores que 255"""
        for i in range(len(matriz_verificada)):
            for j in range(len(matriz_verificada[0])):
                if matriz_verificada[i][j] > 255:
                    matriz_verificada[i][j] = 255

        return matriz_verificada

    def verificarTamanhoSubtracao(self, matriz_verificada):
        """Verificar matriz para valores menores que 0"""
        for i in range(len(matriz_verificada)):
            for j in range(len(matriz_verificada[0])):
                if matriz_verificada[i][j] < 0:
                    matriz_verificada[i][j] = 0

        return matriz_verificada

    def adicao(self):
        return self.verificarTamanhoSoma(self.imagem_1 + self.imagem_2)

    def subtracao(self):
        return self.verificarTamanhoSubtracao(self.imagem_1 - self.imagem_2)

    def operacaoAritmetica(self):
        resultado_soma = self.adicao()
        resultado_subtracao = self.subtracao()
        return np.matrix(resultado_soma), np.matrix(resultado_subtracao)