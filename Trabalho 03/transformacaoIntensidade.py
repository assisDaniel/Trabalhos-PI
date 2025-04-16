from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

imagem_original = Image.open("./Trabalho 03/Quizz2.png").convert("L")

imagem_array = np.array(imagem_original)

imagem_negativa_array = 255 - imagem_array  

imagem_negativa = Image.fromarray(imagem_negativa_array)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original (Cinza)")
plt.imshow(imagem_original, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Negativa")
plt.imshow(imagem_negativa, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()
