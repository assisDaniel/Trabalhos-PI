import numpy as np


class Reflexao:
    def __init__(self, imagem):
        self.image = np.array(imagem)
        self.height, self.width = self.image.shape

    def reflexaoVertical(self):
        imagemRefletida = [
            [[0 for _ in range(self.height)] for _ in range(self.width)]
            for _ in range(self.height)
        ]

        for j in range(self.width):
            for i in range(self.height):
                imagemRefletida[i][j] = self.image[i][self.width - j - 1]

        return np.matrix(imagemRefletida)

    def reflexaoHorizontal(self):
        imagemRefletida = [
            [[0 for _ in range(self.width)] for _ in range(self.width)]
            for _ in range(self.height)
        ]

        for i in range(self.height):
            for j in range(self.width):
                imagemRefletida[i][j] = self.image[self.height - i - 1][j]

        return np.matrix(imagemRefletida)