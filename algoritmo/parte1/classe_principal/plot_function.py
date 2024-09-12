import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class PlotFunction():
    def __init__(self) -> None:
        pass

    @staticmethod
    def plot(func, amostras, limite):
        # Gerar 500 pontos no intervalo definido por limite
        x1 = np.linspace(limite[0,0], limite[0,1], 500)
        x2 = np.linspace(limite[1,0], limite[1,1], 500)

        # Criar a malha 2D de pontos
        x1, x2 = np.meshgrid(x1, x2)

        # Avaliar a função para cada par (x1, x2) da malha
        z = func(x1, x2)

        # Configurar a figura
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Tornar a superfície um pouco transparente
        ax.plot_surface(x1, x2, z, rstride=10, cstride=10, cmap='viridis', alpha=0.6)

        # Coordenadas das amostras
        amostra_x1 = [amostra[0] for amostra in amostras]
        amostra_x2 = [amostra[1] for amostra in amostras]
        amostra_z = [amostra[2] for amostra in amostras]

        # Plotar os pontos amostra sobre o gráfico, com zorder alto para ficar em primeiro plano
        ax.scatter(amostra_x1, amostra_x2, amostra_z, 
                   color='r',          # Cor vermelha para os pontos
                   s=100,              # Tamanho maior dos pontos
                   edgecolor='k',      # Borda preta ao redor dos pontos
                   zorder=5,           # Valor alto para renderizar os pontos na frente
                   label='Pontos Amostra')

        # Adicionar rótulos e legenda
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('f(x1, x2)')
        ax.legend()

        # Exibir o gráfico
        plt.show()