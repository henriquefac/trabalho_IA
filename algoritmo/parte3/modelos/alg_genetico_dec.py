import numpy as np

class Alg_gen_dec():
    def __init__(self, eta, pop_size, max_generation, restricoes, crossover_rate=0.85,
                 mutation_rate=0.01, A=10, p=20, sigma=0.1, tournament_size=3):
        self.A = A
        self.p = p
        self.eta = eta
        self.restricoes = restricoes
        self.pop_size = pop_size
        self.max_generation = max_generation
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.sigma = sigma  # Desvio padrão para a mutação gaussiana
        self.tournament_size = tournament_size  # Tamanho do torneio para seleção

    # Função objetiva para minimizar
    def funcao_objetiva(self, x):
        return self.A * len(x) + np.sum(x**2 - self.A * np.cos(2 * np.pi * x))
    
    # Função de aptidão
    def f_apt(self, x):
        return self.funcao_objetiva(x) + 1
    
    # geração de indivíduos
    def gerar_individuo(self):
        return np.random.uniform(self.restricoes[0], self.restricoes[1], self.p)
    # gerar populacao
    def gerar_populacao(self):
        return np.array([self.gerar_individuo() for _ in range(self.pop_size)])
    

    # Recombinação (crossover) por SBX
    def crossover_SBX(self, pai1, pai2):
        u = np.random.uniform(size=len(pai1))
        beta = np.where(u <=0.5, (2 * u) ** (1/(self.eta + 1)), (1 / (2 * (1 - u)))**(1 / (self.eta + 1)))
        c1 = np.clip(0.5 * ((pai1 + pai2) - beta * (pai2 - pai1)), self.restricoes[0], self.restricoes[1])
        c2 = np.clip(0.5 * ((pai1 + pai2) + beta * (pai2 - pai1)), self.restricoes[0], self.restricoes[1])
        return c1, c2
    def mutacao_gaussiana(self, individuo):
        perturbacoes = np.random.normal(0, self.sigma, size=individuo.shape)
        for i in range(len(individuo)): 
            if np.random.rand() < self.mutation_rate: 
                individuo[i] += perturbacoes[i]  
                individuo[i] = np.clip(individuo[i], self.restricoes[0], self.restricoes[1])  
        return individuo

    # Seleção por torneio
    def selecao_torneio(self, populacao, aptidao):
        indices = np.random.choice(len(populacao), self.tournament_size, replace=False)
        melhor_indice = indices[np.argmin(np.array(aptidao)[indices])]
        return populacao[melhor_indice]
    
    # convergência
    def convergencia(self, aptidao):
        for apt in aptidao:
            if apt < 100:
                return True
        return False
    # Criar nova geração
    def new_generation(self, populacao, aptidao):
        new_pop = []
        for _ in range(self.pop_size // 2):
            pai1 = self.selecao_torneio(populacao, aptidao)
            pai2 = self.selecao_torneio(populacao, aptidao)

            if np.random.rand() < self.crossover_rate:
                f1, f2 = self.crossover_SBX(pai1, pai2)
            else:
                f1, f2 = np.copy(pai1), np.copy(pai2)

            # Aplicar mutação
            f1 = self.mutacao_gaussiana(f1)
            f2 = self.mutacao_gaussiana(f2)

            new_pop.extend([f1, f2])

        return np.array(new_pop)
    
    # Executar o algoritmo genético
    def executar(self):
        mean_per_pop = list()
        populacao = self.gerar_populacao()
        for geracao in range(self.max_generation):
            aptidao = [self.f_apt(ind) for ind in populacao]
            mean_per_pop.append(np.mean(aptidao))
            # verificar parada por convergência
            if self.convergencia(aptidao):
                if __name__ == "__main__":
                    print("parada por convergencia")
                break

            populacao = self.new_generation(populacao, aptidao)

            
        # Retornar o melhor indivíduo encontrado
        aptidao = [self.f_apt(ind) for ind in populacao]
        melhor_indice = np.argmin(aptidao)
        return populacao[melhor_indice], populacao, mean_per_pop


# Exemplo de uso
if __name__ == "__main__":
    eta = 1
    pop_size = 100
    max_generation = 1000
    restricoes = (-10, 10)  # Limites para a função objetivo
    alg_gen = Alg_gen_dec(eta, pop_size, max_generation, restricoes)

    melhor_individuo, best_pop = alg_gen.executar()
    print(f"Melhor indivíduo encontrado: {melhor_individuo}")
    print(f"Apitidão do melhor indivíduo: {alg_gen.f_apt(melhor_individuo)}")