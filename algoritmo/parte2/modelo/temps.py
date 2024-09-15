import numpy as np

class Temperatura_Simulada():
    def __init__(self, quantidade_variaveis, funcao_opt, funcao_amostra, 
                 pertubar, temperatura=100, decay=0, iteracao = 10000, min = False) -> None:
        # definir parâmetros de têmpera

        # Quantidade de variáveis
        self.n = quantidade_variaveis

        # Valor da temperatura inicial (float)
        self.temperatura = temperatura

        # maximizar/minimizar
        self.aval = lambda f_cand, f_opt: f_cand > f_opt 
        if min:
            self.aval = lambda f_cand, f_opt: f_cand < f_opt


        # iteracoes máxima
        self.iteracoes = iteracao


        # Funções

        # função usada para pertubar ultima solução
        self.pertubar = pertubar

        # funcao para gerar amostra
        self.funcao_amostra = funcao_amostra

        # Função para avaliar a qualidade da amostra
        self.funcao_opt = funcao_opt

        # Função de escalonamento (decay) para reduzir a temperatura
        if decay ==0:
            self.decay = self.default_decay
        elif decay == 1:
            self.decay = self.deacay_1
        else:
            self.decay = self.decay_2

    def default_decay(self, t, i):

        return t * 0.99
    
    def deacay_1(self, t, i):
        return t/(1+0.99*np.sqrt(t))
    
    def decay_2(self, t, i):
        delta = (t - self.temperatura)/(i+1)
        return t - delta


    def aceitacao(sale, f_cand, f_opt, temperatura):
        return np.exp(- ((f_cand - f_opt)/ temperatura))

    def optmizar(self):
        # primiero candidato
        x_opt = self.funcao_amostra()
        temp = self.temperatura
        # qualidade da amostra
        f_opt = self.funcao_opt(x_opt)
        for i in range(self.iteracoes):
            x_cand = self.pertubar(x_opt)
            f_cand = self.funcao_opt(x_cand)

            if f_cand == 28:
                x_opt = x_cand
                f_opt = f_cand
                break
            if self.aval(f_cand, f_opt) or np.random.rand() < self.aceitacao(f_cand, f_opt, temp):
                x_opt = x_cand
                f_opt = f_cand
            

            temp = self.decay(temp, i)



        return x_opt, f_opt