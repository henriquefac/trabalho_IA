import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.animation as animation

class plot_table():
    def __init__(self) -> None:
        pass

    @staticmethod
    def create_table_lines(array):
        list_cord = list()
        # Criar o tabuleiro com padrão de xadrez
        table = np.full((8, 8), 0)
        for i in range(8):
            f = i % 2 == 0
            for j in range(8):
                if not f:
                    table[i, j] += 1
                f = not f 
        for i in range(len(array)):
            aux_list = list()
            for j in range(i + 1, len(array)):
                dif = np.abs(j - i)
                linha1 = len(array) - array[i] - 1 + dif
                linha2 = len(array) - array[i] - 1 - dif
                if linha1 in list(range(8)):
                    aux_list.append((linha1, j))
                if linha2 in list(range(8)):
                    aux_list.append((linha2, j))
            list_cord.append(aux_list)

        # Posicionar as rainhas (sem as linhas de ameaça)
        for i in range(len(array)):
            table[len(array) - array[i] - 1, i] = 2  # 2 será usado para indicar as peças (rainhas)
        
        return table.reshape((8, 8)), list_cord

    @staticmethod
    def Pboard_lines(array):
        # Criar o tabuleiro
        table, list_cord = plot_table.create_table_lines(array)

        # Definir as cores - 0 para branco, 1 para preto e 2 para roxo (peças)
        cores = ["white", "black", "purple"]  # purple para as peças (rainhas)

        # Criar um colormap com as cores definidas
        cmap = mcolors.ListedColormap(cores)

        # Plotar o tabuleiro com as rainhas
        plt.figure(figsize=(6, 6))
        plt.imshow(table, cmap=cmap)

        # Traçar as linhas de ameaça
        for i in range(len(list_cord)):
            # Coordenada inicial para traçar a linha (posição da rainha)
            cordenada0 = (7 - array[i], i)  # (linha, coluna)
            for j in range(len(list_cord[i])):
                # Coordenada final da linha (onde há ameaça)
                cordenada1 = list_cord[i][j]
                # Traçar linha vermelha que indica zona de ameaça
                plt.plot([cordenada0[1], cordenada1[1]], [cordenada0[0], cordenada1[0]], color='red', linewidth=1.5)

        plt.show()

    @staticmethod
    def create_table(array):

        # Criar o tabuleiro com padrão de xadrez
        table = np.full((8, 8), 0)
        for i in range(8):
            f = i % 2 == 0
            for j in range(8):
                if not f:
                    table[i, j] += 1
                f = not f 


        # Posicionar as rainhas (sem as linhas de ameaça)
        for i in range(len(array)):
            table[len(array) - array[i] - 1, i] = 2  # 2 será usado para indicar as peças (rainhas)
        
        return table.reshape((8, 8))

    @staticmethod
    def Pboard(array):
        # Criar o tabuleiro
        table = plot_table.create_table(array)

        # Definir as cores - 0 para branco, 1 para preto e 2 para roxo (peças)
        cores = ["white", "black", "purple"]  # purple para as peças (rainhas)

        # Criar um colormap com as cores definidas
        cmap = mcolors.ListedColormap(cores)

        # Plotar o tabuleiro com as rainhas
        plt.figure(figsize=(6, 6))
        plt.imshow(table, cmap=cmap)


        plt.show()

    # gerar gif das plotagens

    @staticmethod
    def sub_plots(array, ax):
        # Criar o tabuleiro
        table = plot_table.create_table(array)

        # Definir as cores - 0 para branco, 1 para preto e 2 para roxo (peças)
        cores = ["white", "black", "purple"]

        # Criar um colormap com as cores definidas
        cmap = mcolors.ListedColormap(cores)

        # Plotar o tabuleiro com as rainhas
        ax.clear()
        ax.imshow(table, cmap=cmap)
        ax.set_xticks([])
        ax.set_yticks([])
    @staticmethod
    def generate_gif(distributions, filename):
        fig, ax = plt.subplots(figsize=(6, 6))

        def update(frame):
            plot_table.sub_plots(distributions[frame], ax)
            ax.set_title(f"Distribuição {frame+1}")

        # Criar a animação
        ani = animation.FuncAnimation(fig, update, frames=len(distributions), repeat=True)

        # Salvar a animação como GIF
        ani.save(filename, writer='pillow', fps=1)  # fps ajusta a velocidade do GIF
        plt.close()
    
    @staticmethod
    def plot_all_projections(distributions):
        num_plots = len(distributions)
        grid_size = int(np.ceil(np.sqrt(num_plots)))  # Determinar o tamanho da grade

        fig, axes = plt.subplots(grid_size, grid_size, figsize=(12, 12))

        for i, ax in enumerate(axes.flat):
            if i < num_plots:
                plot_table.sub_plots(distributions[i], ax)
                ax.set_title(f"Proj {i+1}")
            else:
                ax.axis('off')  # Desligar eixos para subplots vazios

        plt.tight_layout()
        plt.show()