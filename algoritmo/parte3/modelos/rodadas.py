import sys
import os
import numpy as np
import pandas as pd  # Para criar a tabela de comparação

sys.path.append(os.path.abspath(r"\Users\henri\Documents\pythonProjcs\trabalho_ia\algoritmo\parte3\modelos"))

from alg_genetico_bit import Alg_gen_bit as alg1
from alg_genetico_dec import Alg_gen_dec as alg2

# Classe para gerenciar as rodadas
class Rodadas():
    def __init__(self, rodadas) -> None:
        self.rodadas = rodadas

    def init_alg_1(self, bit, pop_size, max_generation, restricoes, crossover_rate=0.85,
                 mutation_rate=0.01, A=10, p=20, n_cross=2):
        self.alg_1 = alg1(bit, pop_size, max_generation, restricoes, crossover_rate,
                 mutation_rate, A, p, n_cross)
    
    def init_alg_2(self, eta, pop_size, max_generation, restricoes, crossover_rate=0.85,
                 mutation_rate=0.01, A=10, p=20, sigma=0.1, tournament_size=3):
        self.alg_2 = alg2(eta, pop_size, max_generation, restricoes, crossover_rate,
                 mutation_rate, A, p, sigma, tournament_size)
        
    def run(self):
        # Listas para armazenar os valores de aptidão de cada algoritmo em cada rodada
        alg1_max, alg1_min = [], []
        alg2_max, alg2_min = [], []

        for _ in range(self.rodadas):
            # Rodar o algoritmo 1
            _, populacao_1 = self.alg_1.executar()

            # Rodar o algoritmo 2
            _, populacao_2 = self.alg_2.executar()

            # Coletar aptidões do Algoritmo 1
            aptidoes_1 = [self.alg_1.f_apt(indi) for indi in self.alg_1.mass_convert(populacao_1)]
            alg1_max.append(np.max(aptidoes_1))
            alg1_min.append(np.min(aptidoes_1))

            # Coletar aptidões do Algoritmo 2
            aptidoes_2 = [self.alg_2.f_apt(indi) for indi in populacao_2]
            alg2_max.append(np.max(aptidoes_2))
            alg2_min.append(np.min(aptidoes_2))

        # Tabelas comparativas
        tabela_comparacao, tl = self.comparar_algoritmos(alg1_max, alg1_min, alg2_max, alg2_min)
        print(tabela_comparacao)
        print(tl)

    def comparar_algoritmos(self, alg1_max, alg1_min, alg2_max, alg2_min):
        # Calcular as estatísticas para ambos os algoritmos

        # Algoritmo 1
        alg1_menor_apt = np.min(alg1_min)
        alg1_maior_apt = np.max(alg1_max)
        alg1_media_apt = np.mean(alg1_max)
        alg1_std_apt = np.std(alg1_max)

        # Algoritmo 2
        alg2_menor_apt = np.min(alg2_min)
        alg2_maior_apt = np.max(alg2_max)
        alg2_media_apt = np.mean(alg2_max)
        alg2_std_apt = np.std(alg2_max)

        # Criar uma tabela de comparação com Pandas
        data = {
            'Algoritmo': ['Algoritmo 1', 'Algoritmo 2'],
            'Menor Aptidão': [alg1_menor_apt, alg2_menor_apt],
            'Maior Aptidão': [alg1_maior_apt, alg2_maior_apt],
            'Média Aptidão': [alg1_media_apt, alg2_media_apt],
            'Desvio-Padrão Aptidão': [alg1_std_apt, alg2_std_apt]
        }
        tabela_comparacao = pd.DataFrame(data)
        tabela_latex = tabela_comparacao.to_latex(index=False)
        return tabela_comparacao, tabela_latex
