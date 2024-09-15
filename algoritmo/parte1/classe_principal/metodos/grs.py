import numpy as np

class GRS():
    def __init__(self, limite: np.ndarray, function, min = False, x_array=None, sigma = None) -> None:
        self.func = function
        self.max_tier = 10000
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
        stop = 100
        for _ in range(self.max_tier):
            ultimo_otimo = f_opt
            #criar novo candidato
            x_cand = self.pertubar()
            f_cand = self.func(*x_cand)
            if self.decision(f_cand, f_opt):
                x_opt = x_cand
                f_opt = f_cand
                if np.abs(f_opt - ultimo_otimo) < 10**(-12):
                    count += 1
                else:
                    count = 0
            else:
                # se não houver melhoria, contador aumenta
                count+=1

            if count == stop:
                break
        return x_opt, f_opt
