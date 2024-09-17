import numpy as np
import time
from tqdm import tqdm
import pandas as pd

class Opt_colection():
    def __init__(self) -> None:
        pass
    @staticmethod
    def get_bests(temper):
        # Usar um conjunto para garantir que os resultados sejam únicos
        resultados_unicos = set()

        while len(resultados_unicos) < 92:
            # Obter a solução ótima, assumindo que é uma sequência de inteiros
            resultado = temper.optmizar()[0]
    
            # Converter a sequência de inteiros em uma string
            resultado_str = "".join(map(str, resultado))
            resultados_unicos.add(resultado_str)  # Adicionar a string ao conjunto

        # Converter os resultados únicos para arrays numpy
        lista = [np.array(list(map(int, list(r)))) for r in resultados_unicos]
        return lista

    # tempo de execução
    @staticmethod
    def get_mean_time(temper, optrs):
        tempos = list()
        opt = 0
        subopt = 0
        for _ in tqdm(range(5000)):
            # Obter a solução ótima, assumindo que é uma sequência de inteiros
            init = time.time()
            resul = temper.optmizar()[1]
            tempos.append(time.time() - init)
            if resul == optrs:
                opt += 1
            else:
                subopt +=1
        return f"""
Media do tempo de execução: {np.mean(tempos)};
Resultados ótimos: {opt};
Resultados subótimos: {subopt};
Porcentagem de resultados ótimos: {(opt/5000)*100} 
"""
    
    # rodar o algoritmo até conseguir todas as 92 combinações
    # para conseguir tempo médi, faça isso 100 vezes
    # tempo de execução médio desse processo
    # fazer isso para cada forma de decay
    @staticmethod
    def mean_timer_92(temper):
        full_time = 0
        for _ in range(100):
            initi = time.time()
            Opt_colection.get_bests(temper)
            fim = time.time()
            full_time += (fim - initi)
        return full_time/100
    @staticmethod
    def table_times_dacay(temper1, temper2, temper3):
        time1 = Opt_colection.mean_timer_92(temper1)
        time2 = Opt_colection.mean_timer_92(temper2)
        time3 = Opt_colection.mean_timer_92(temper3)
        data = {
            "Escalonamento": ["Escalonamento padrão", "Escalonamento 1", "Escalonamento 2"],
            "Tempo médio: 92 soluções ótimas":[time1, time2, time3]
        }
        return data
        

    