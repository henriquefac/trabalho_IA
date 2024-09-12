import numpy as np

class GRS():
    def __init__(self, desvio, limite: np.ndarray, function, min = False, x_array=None) -> None:
        self.func = function
        self.max_tier = 10000
        self.desvio = desvio
        self.limite = limite
        if x_array is None:
            self.x_array = np.array([
                np.random.uniform(limite[0,0], limite[0,1]),
                np.random.uniform(limite[1,0], limite[1,1])
            ])
        # se candidato for maior que o ótimo atual
        self.decision = lambda cand, opt: cand > opt
        if min:
            self.decision = lambda cand, opt: cand < opt
        
    def dist(self, limite):
        l1, l2 = limite
        cand = np.random.uniform(l1, l2)
        return cand

    def pertubar(self):
        return np.array([self.dist(l) for l in self.limite])

    def optmizer(self):
        x_array = np.array([
                np.random.uniform(self.limite[0,0], self.limite[0,1]),
                np.random.uniform(self.limite[1,0], self.limite[1,1])
            ])
        x_opt = np.copy(x_array)
        f_opt = self.func(*x_opt)
        
        count = 0
        last_val = f_opt
        for _ in range(self.max_tier):
            #criar novo candidato
            x_cand = self.pertubar()
            f_cand = self.func(*x_cand)
            if self.decision(f_cand, f_opt):
                x_opt = x_cand
                f_opt = f_cand
            #print(x_opt)
                    # Verifica a condição de parada
            if count == 20:
                if np.abs(last_val - f_opt) < 0.000000001:
                    
                    break
                else:
                    count = 0
                    last_val = f_opt
            count += 1
        return x_opt, f_opt
