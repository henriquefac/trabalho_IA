import numpy as np

class Hill_climb():
    def __init__(self, limite: np.ndarray, function,x_array: np.ndarray, min = False, sigma = None) -> None:
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
        stop = 100
        for _ in range(self.max_tier):
            #criar novo candidato
            ultimo_otimo = f_opt
            x_cand = self.pertubar(x_opt)
            f_cand = self.func(*x_cand)
            if self.decision(f_cand, f_opt):
                x_opt = x_cand
                f_opt = f_cand
                # se a melhoria tiver uma diferença com o ultimo ótimo
                # maior que 10^-6, contador não aumenta e retorna a 0 
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
