from PIL import Image

# Tente abrir a imagem
try:
    imagem = Image.open("lena.png").convert("L")
except FileNotFoundError:
    print("Imagem não encontrada. Verifique o nome do arquivo.")
    exit()

largura, altura = imagem.size
pixels = list(imagem.getdata())
print(f"Total de pixels: {len(pixels)}")

# === 1. REDUZIR PARA 8 NÍVEIS DE CINZA (Rk) ===
rk = [pixel for pixel in pixels]  # 256/8 = 32

# === 2. CALCULAR HISTOGRAMA DE 8 NÍVEIS (Nk) ===
nk = [0] * 256
for pixel in rk:
    nk[pixel] += 1



# === 3. CALCULAR HISTOGRAMA NORMALIZADO (Pr) ===
totalPixels = largura * altura
pr = [(qtd / totalPixels)for qtd in nk]
print('Pr len:',len(pr))

# === 4. CÁLCULO DA Freq (frequência acumulada) ===
freq = [0] * 256
acumulado = 0
for i in range(256):
    acumulado += pr[i]
    freq[i] = acumulado

# === 5. CALCULAR A EQ (equalização) ===
# Conforme os slides: eq[i] = (L-1) * pr[i]
eq = [0]*256
acumulado = 0
for i in range(256):
    acumulado += 255*pr[i]
    eq[i] = round(acumulado)

print('len eq',len(eq))
print(eq)

# === 6. APLICAR A EQUALIZAÇÃO NOS PIXELS ===
pixelsEqualizados = [eq[nivel] for nivel in rk]

conversao = [int(p * 255 / 7) for p in eq]
print(conversao)

print(f"Total de pixels equalizados: {len(pixelsEqualizados)}")

# === 7. REESCALAR PARA 0–255 PARA VISUALIZAÇÃO E SALVAR ===
# pixels255 = [int(p * 255 / 7) for p in pixelsEqualizados]

novaImagem = Image.new("L", (largura, altura))
novaImagem.putdata(pixelsEqualizados)
novaImagem.save("resultado.png")
novaImagem.show()

