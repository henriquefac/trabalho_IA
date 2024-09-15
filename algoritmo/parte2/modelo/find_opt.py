import numpy as np
import time
from tqdm import tqdm

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
        # Usar um conjunto para garantir que os resultados sejam únicos
        tempos = list()
        subopt_resuls = list()
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

    