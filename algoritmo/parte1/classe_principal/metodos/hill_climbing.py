import numpy as np

class Hill_climb():
    def __init__(self, sigma, limite: np.ndarray, function,x_array: np.ndarray, min = False) -> None:
        self.func = function
        self.max_tier = 10000
        self.sigma = sigma
        self.limite = limite
        self.x_array = x_array
        # se candidato for maior que o ótimo atual
        self.decision = lambda cand, opt: cand > opt
        if min:
            self.decision = lambda cand, opt: cand < opt
        
    def dist(self, x, limite):
        l1, l2 = limite
        cand = np.clip(np.random.uniform(low=x-self.sigma, high=x+self.sigma), l1, l2)
        return cand

    def pertubar(self, x_array):
        return np.array([self.dist(x, l) for x, l in zip(x_array, self.limite)])

    def optmizer(self, x_array=None):
        if x_array == None:
            x_array = self.x_array
        x_opt = np.copy(x_array)
        f_opt = self.func(*x_opt)
        
        count = 0
        last_val = f_opt
        for _ in range(self.max_tier):
            #criar novo candidato
            x_cand = self.pertubar(x_opt)
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
