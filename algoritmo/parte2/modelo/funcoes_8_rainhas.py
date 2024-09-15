import numpy as np

# função para pertubar uma amostra de um array das 8 rainhas
def perturb(qunt):
    def function(array):
        # novo array
        x_cand = np.copy(array)
        poicoes = np.random.choice(len(array), qunt, replace= False)
        x_cand[poicoes] = np.random.permutation(x_cand[poicoes])

        return x_cand
    return function


# funcao para avliar qaulidade da amostra
# quantidade de pares que não se atacam na distribuição
def f(array):
    atks = 0
    for i in range(len(array)):
        for n in range(i + 1, len(array)):  # Evita comparar a mesma posição
            # Verifica se estão na mesma diagonal ou na mesma linha
            if np.abs(n - i) == np.abs(array[i] - array[n]) or array[i] == array[n]:
                atks += 1

    return 28 - atks 



# funcao para gerar candidato dentro do limite

def amostra():
    return np.random.permutation(8)