import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class InterpolacaoBilinear:
    def __init__(self, caminho_imagem):
        self.imagens = self.ler_imagens(caminho_imagem)
    
    def ler_imagens(self, caminho):
        """Lê uma imagem ou uma lista de imagens e as converte para matrizes NumPy"""
        if isinstance(caminho, list):
            imagens = []
            for caminho_img in caminho:
                img = Image.open(caminho_img).convert('L') 
                imagens.append(np.array(img))
            return imagens
        else:
            img = Image.open(caminho).convert('L') 
            return [np.array(img)]
    
    def reduzir(self, matriz):
        """Reduz a matriz calculando a média de blocos 2x2"""
        linhas, colunas = matriz.shape
        linhas_reduzidas = (linhas ) // 2
        colunas_reduzidas = (colunas) // 2
        
        nova_matriz = np.zeros((linhas_reduzidas, colunas_reduzidas), dtype=matriz.dtype)
        
        for i in range(linhas_reduzidas):
            for j in range(colunas_reduzidas):
                i_orig = i * 2
                j_orig = j * 2
                
                i_orig_2 = min(i_orig + 1, linhas - 1)
                j_orig_2 = min(j_orig + 1, colunas - 1)
                
                pixels = [
                    matriz[i_orig, j_orig],
                    matriz[i_orig, j_orig_2],
                    matriz[i_orig_2, j_orig],
                    matriz[i_orig_2, j_orig_2]
                ]
                nova_matriz[i, j] = np.round(np.mean(pixels)).astype(matriz.dtype)
                
        return nova_matriz
   
    def ampliar(self, matriz):
        """Amplia a matriz usando interpolação bilinear exatamente como mostrado na imagem"""
        linhas, colunas = matriz.shape
        linhas_novas = (linhas * 2) - 1
        colunas_novas = (colunas * 2) - 1
        
        nova_matriz = np.zeros((linhas_novas, colunas_novas), dtype=matriz.dtype)
        
        for i in range(linhas):
            for j in range(colunas):
                nova_matriz[i*2, j*2] = matriz[i, j]
        
        for i in range(0, linhas_novas, 2):  
            for j in range(1, colunas_novas, 2): 
                if j+1 < colunas_novas:
                    nova_matriz[i, j] = round((nova_matriz[i, j-1] + nova_matriz[i, j+1]) / 2)
        
        for i in range(1, linhas_novas, 2):  
            for j in range(0, colunas_novas, 2):
                if i+1 < linhas_novas:
                    nova_matriz[i, j] = round((nova_matriz[i-1, j] + nova_matriz[i+1, j]) / 2)
        
        for i in range(1, linhas_novas, 2):
            for j in range(1, colunas_novas, 2):
                if i+1 < linhas_novas and j+1 < colunas_novas:
                    nova_matriz[i, j] = np.round(np.mean((
                        nova_matriz[i-1, j-1] + 
                        nova_matriz[i-1, j+1] + 
                        nova_matriz[i+1, j-1] + 
                        nova_matriz[i+1, j+1]
                    ) / 4)).astype(dtype=matriz.dtype)
                    
        return nova_matriz
    
    def processar_imagens(self):
        """Processa todas as imagens para reduzir e ampliar"""
        resultados_reduzidos = []
        resultados_ampliados = []
        
        for matriz in self.imagens:
            matriz_reduzida = self.reduzir(matriz)
            resultados_reduzidos.append(matriz_reduzida)
            
            matriz_ampliada = self.ampliar(matriz)
            resultados_ampliados.append(matriz_ampliada)
        
        return resultados_reduzidos, resultados_ampliados
    
    def salvar_imagens(self, matrizes_reduzidas, matrizes_ampliadas, prefixo_saida="output_bilinear"):
        """Salva as matrizes como imagens"""
        for i, (matriz_reduzida, matriz_ampliada) in enumerate(zip(matrizes_reduzidas, matrizes_ampliadas)):
            img_reduzida = Image.fromarray(matriz_reduzida.astype(np.uint8))
            caminho_reduzida = f"{prefixo_saida}_reduzida_{i}.png"
            img_reduzida.save(caminho_reduzida)
            
            img_ampliada = Image.fromarray(matriz_ampliada.astype(np.uint8))
            caminho_ampliada = f"{prefixo_saida}_ampliada_{i}.png"
            img_ampliada.save(caminho_ampliada)
            
        print(f"Todas as imagens reduzidas e ampliadas foram salvas com o prefixo '{prefixo_saida}'")
    
    def mostrar_resultados(self, matrizes_reduzidas, matrizes_ampliadas):
        """Mostra os resultados das imagens (útil para notebooks)"""
        for i, (matriz_original, matriz_reduzida, matriz_ampliada) in enumerate(zip(self.imagens, matrizes_reduzidas, matrizes_ampliadas)):
            plt.figure(figsize=(15, 5))
            
            plt.subplot(1, 3, 1)
            plt.imshow(matriz_original, cmap='gray')
            plt.title(f"Original {i}")
            
            plt.subplot(1, 3, 2)
            plt.imshow(matriz_reduzida, cmap='gray')
            plt.title(f"Reduzida {i}")
            
            plt.subplot(1, 3, 3)
            plt.imshow(matriz_ampliada, cmap='gray')
            plt.title(f"Ampliada {i}")
            
            plt.tight_layout()
            plt.show()