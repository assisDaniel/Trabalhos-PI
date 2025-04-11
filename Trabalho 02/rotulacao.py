import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def rotulacao_componentes_conectados(imagem_binaria):
    if np.max(imagem_binaria) > 1:
        imagem_binaria = (imagem_binaria > 0).astype(np.int32)

    imagem_binaria = imagem_binaria.astype(np.int32)
    linhas, colunas = imagem_binaria.shape
    imagem_rotulada = np.zeros((linhas, colunas), dtype=np.int32)
    rotulo_atual = 1
    equivalencias = {}

    for y in range(linhas):
        for x in range(colunas):
            p = imagem_binaria[y, x]
            if p == 0:
                continue  # Se p = 0 então verifica o próximo pixel

            # Examina os vizinhos r (esquerda) e t (acima)
            r = imagem_rotulada[y, x-1] if x > 0 else 0
            t = imagem_rotulada[y-1, x] if y > 0 else 0

            if r == 0 and t == 0:
                # então rotula p com novo rótulo
                imagem_rotulada[y, x] = rotulo_atual
                equivalencias[rotulo_atual] = rotulo_atual
                rotulo_atual += 1
            elif (r != 0 and t == 0) or (r == 0 and t != 0):
                # rotula p com o rótulo de r ou de t
                imagem_rotulada[y, x] = r if r != 0 else t
            elif r != 0 and t != 0:
                if encontrar_rotulo_raiz(equivalencias, r) == encontrar_rotulo_raiz(equivalencias, t):
                    # possuem o mesmo rótulo, então rotula p com este rótulo
                    imagem_rotulada[y, x] = encontrar_rotulo_raiz(equivalencias, r)
                else:
                    # possuem rótulos diferentes, então rotula p com um dos rótulos e indica equivalência
                    raiz_r = encontrar_rotulo_raiz(equivalencias, r)
                    raiz_t = encontrar_rotulo_raiz(equivalencias, t)
                    imagem_rotulada[y, x] = raiz_r
                    equivalencias[raiz_t] = raiz_r

    # Segunda passagem: resolve equivalências
    rotulos_resolvidos = {}
    proximo_rotulo = 1
    for rotulo in range(1, rotulo_atual):
        raiz = encontrar_rotulo_raiz(equivalencias, rotulo)
        if raiz not in rotulos_resolvidos:
            rotulos_resolvidos[raiz] = proximo_rotulo
            proximo_rotulo += 1

    for y in range(linhas):
        for x in range(colunas):
            if imagem_rotulada[y, x] > 0:
                raiz = encontrar_rotulo_raiz(equivalencias, imagem_rotulada[y, x])
                imagem_rotulada[y, x] = rotulos_resolvidos[raiz]

    return imagem_rotulada, proximo_rotulo - 1


def encontrar_rotulo_raiz(equivalencias, rotulo):
    if equivalencias[rotulo] != rotulo:
        equivalencias[rotulo] = encontrar_rotulo_raiz(equivalencias, equivalencias[rotulo])
    return equivalencias[rotulo]

def visualizar_imagem_rotulada(imagem_rotulada, num_rotulos):
    np.random.seed(42)
    cores = np.vstack(([0, 0, 0], np.random.rand(num_rotulos, 3)))
    imagem_rgb = cores[imagem_rotulada]
    plt.figure(figsize=(12, 10))
    plt.imshow(imagem_rgb)
    plt.title(f'Componentes Conectados (Total: {num_rotulos})')
    plt.axis('off')
    plt.savefig('componentes_rotulados.png')
    plt.show()
    print(f"Imagem salva como 'componentes_rotulados.png'")
    return imagem_rgb

def processar_imagem(caminho_imagem, limiar=127):
    try:
        imagem = Image.open(caminho_imagem)
        if imagem.mode != 'L':
            imagem = imagem.convert('L')
        imagem_original = np.array(imagem)
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        return None, None, None, None, 0
    imagem_binaria = (imagem_original <= limiar).astype(np.int32)
    imagem_rotulada, num_rotulos = rotulacao_componentes_conectados(imagem_binaria)
    imagem_rgb = visualizar_imagem_rotulada(imagem_rotulada, num_rotulos)
    return imagem_original, imagem_binaria, imagem_rotulada, imagem_rgb, num_rotulos

def salvar_resultados(imagem_original, imagem_binaria, imagem_rotulada, imagem_rgb, pasta_saida='resultados'):
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
    Image.fromarray(imagem_original).save(os.path.join(pasta_saida, 'original.png'))
    Image.fromarray(imagem_binaria.astype(np.uint8) * 255).save(os.path.join(pasta_saida, 'binaria.png'))
    max_label = np.max(imagem_rotulada)
    if max_label > 0:
        norm_rotulada = (imagem_rotulada * 255 / max_label).astype(np.uint8)
    else:
        norm_rotulada = np.zeros_like(imagem_rotulada, dtype=np.uint8)
    Image.fromarray(norm_rotulada).save(os.path.join(pasta_saida, 'rotulada_gray.png'))
    imagem_rgb_uint8 = (imagem_rgb * 255).astype(np.uint8)
    Image.fromarray(imagem_rgb_uint8).save(os.path.join(pasta_saida, 'rotulada_color.png'))
    print(f"Todas as imagens foram salvas na pasta '{pasta_saida}'")

def mostrar_interface_usuario():
    print("=" * 60)
    print("ROTULAÇÃO DE COMPONENTES CONECTADOS EM IMAGENS BINÁRIAS")
    print("=" * 60)
    caminho_imagem = "/home/assisdaniel/Documentos/UFT/6º Período/Processamento de Imagens/Implementações/asasas/Trabalho 02/image1.png"
    if not os.path.isfile(caminho_imagem):
        print(f"ERRO: O arquivo '{caminho_imagem}' não existe.")
        return
    try:
        limiar = int(input("Digite o valor limiar para binarização (0-255): "))
        if limiar < 0 or limiar > 255:
            print("ERRO: Limiar deve estar entre 0 e 255. Usando valor padrão 127.")
            limiar = 127
    except ValueError:
        print("ERRO: Valor inválido. Usando limiar padrão 127.")
        limiar = 127
    print("\nProcessando imagem...")
    imagem_original, imagem_binaria, imagem_rotulada, imagem_rgb, num_rotulos = processar_imagem(
        caminho_imagem, limiar
    )
    if imagem_original is None:
        return
    print(f"\nForam encontrados {num_rotulos} componentes conectados.")
    salvar = input("\nDeseja salvar todos os resultados? (s/n): ").lower()
    if salvar == 's':
        pasta_saida = input("Digite o nome da pasta de saída (padrão: 'resultados'): ")
        if not pasta_saida:
            pasta_saida = 'resultados'
        salvar_resultados(imagem_original, imagem_binaria, imagem_rotulada, imagem_rgb, pasta_saida)

if __name__ == "__main__":
    mostrar_interface_usuario()
