import numpy as np

class Alg_gen_bit:
    def __init__(self, bit, pop_size, max_generation, restricoes, crossover_rate=0.85,
                 mutation_rate=0.01, A=10, p=20, n_cross=2):
        self.A = A
        self.p = p
        self.bit = bit
        self.restricoes = restricoes
        self.pop_size = pop_size
        self.max_generation = max_generation
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.n_cross = n_cross

    # Função objetiva para minimizar
    def funcao_objetiva(self, x):
        return self.A * len(x) + np.sum(x**2 - self.A * np.cos(2 * np.pi * x))
    
    # Função de aptidão
    def f_apt(self, x):
        return self.funcao_objetiva(x) + 1
    
    # Geração de indivíduo
    def gerar_individuo(self):
        return np.random.randint(0, 2, self.p * self.bit)

    # Geração da população inicial
    def gerar_populacao(self):
        return np.array([self.gerar_individuo() for _ in range(self.pop_size)])
    
    # Função para converter de bit para decimal
    def phi(self, segment):
        decimal = 0
        for i in range(len(segment)):
            decimal += segment[i] * 2 ** (len(segment) - 1 - i)
        
        # Normalizar para os limites
        max_val = 2 ** len(segment) - 1
        true_val = self.restricoes[0] + (self.restricoes[1] - self.restricoes[0]) * decimal / max_val
        return true_val
    
    def convert(self, array_bits):
        return np.array([self.phi(array_bits[i*self.bit: (i+1)*self.bit]) for i in range(self.p)])

    def mass_convert(self, populacao):
        return np.array([self.convert(individual) for individual in populacao])
    
    # Realizar cruzamento de candidatos
    def crossover(self, pai1, pai2):
        pontos_corte = np.sort(np.random.choice(len(pai1), self.n_cross, replace=False))
        f1, f2 = np.copy(pai1), np.copy(pai2)

        for i in range(self.n_cross):
            inicio = pontos_corte[i]
            fim = pontos_corte[i+1] if i+1 < len(pontos_corte) else len(pai1)

            if i % 2 == 0:  # Troca segmentos nos filhos
                f1[inicio:fim] = pai2[inicio:fim]
                f2[inicio:fim] = pai1[inicio:fim]

        return f1, f2
    
    # Método da roleta para escolha
    def roleta(self, populacao, aptidoes):
        fitness_invertido = 1 / (aptidoes + 1e-10)
        total_fitness = np.sum(fitness_invertido)
        probabilidades = fitness_invertido / total_fitness
        
        r = np.random.uniform()
        acumulado = 0.0
        for i, prob in enumerate(probabilidades):
            acumulado += prob
            if acumulado > r:
                return populacao[i]
        return populacao[-1]
    
    # Mutação fora de ordem
    def mutacao(self, individuo):
        for i in range(len(individuo)):
            if np.random.rand() < self.mutation_rate:
                individuo[i] = 1 - individuo[i]  # Inverte o bit
        return individuo
    
    # Criar nova geração
    def new_generation(self, populacao, aptidoes):
        new_pop = []

        for _ in range(self.pop_size // 2):
            pai1 = self.roleta(populacao, aptidoes)
            pai2 = self.roleta(populacao, aptidoes)
            
            if np.random.rand() < self.crossover_rate:
                f1, f2 = self.crossover(pai1, pai2)
            else:
                f1, f2 = np.copy(pai1), np.copy(pai2)
            
            f1 = self.mutacao(f1)
            f2 = self.mutacao(f2)

            new_pop.extend([f1, f2])
        
        return np.array(new_pop)
    
    # Verificar população para saber se algum indivíduo satisfaz o critério
    def verificar_criterio(self, populacao):
        aptidoes = np.array([self.f_apt(self.convert(individual)) for individual in populacao])
        melhor_aptidao = np.min(aptidoes)
        if melhor_aptidao < 100:  # Critério de convergência (exemplo)
            return True
        return False
    
    def executar(self):
        mean_per_pop = list()
        populacao = self.gerar_populacao()
        

        for geracao in range(self.max_generation):
            aptidoes = np.array([self.f_apt(self.convert(individual)) for individual in populacao])

            mean_per_pop.append(np.mean(aptidoes))

            if self.verificar_criterio(populacao):
                if __name__ == "__main__":
                    print(f"Convergência alcançada na geração {geracao}")
                break
            
            populacao = self.new_generation(populacao, aptidoes)
        
        # Melhor solução encontrada
        aptidoes = np.array([self.f_apt(self.convert(individual)) for individual in populacao])
        melhor_individuo = populacao[np.argmin(aptidoes)]
        melhor_aptidao = np.min(aptidoes)
        return melhor_individuo, populacao, mean_per_pop


if __name__ == "__main__":
    # Exemplo de uso
    alg_gen = Alg_gen_bit(bit=15, pop_size=100, max_generation=1000, restricoes=(-10, 10), n_cross=1)
    melhor_individuo, populacao = alg_gen.executar()
    print(alg_gen.f_apt(alg_gen.convert(melhor_individuo)))
    print(melhor_individuo)
