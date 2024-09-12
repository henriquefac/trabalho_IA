import numpy as np
class Teste_rounds():
    def __init__(self,obj) -> None:
        self.test_obj = obj
    
    def rounds(self):
        self.lista_solucoes = list()
        self.lista_ress = list()
        for _ in range(100):
            tot = (self.test_obj.optmizer())
            self.lista_solucoes.append(tot[0])
            self.lista_ress.append(tot[1])
        