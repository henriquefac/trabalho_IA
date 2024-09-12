from classe_principal.metodos.hill_climbing import Hill_climb
from classe_principal.metodos.grs import GRS
from classe_principal.metodos.lrs import LRS
import numpy as np



def ex1(classe, sigma_desvio, x_opt=None):
    limite = np.array(
        [[-100, 100],
        [-100, 100]]
    )
    def func(x1, x2):
        return np.power(x1, 2) + np.power(x2, 2)


    return classe(sigma_desvio, limite, func, min = True, x_array = x_opt)

def ex2(classe, sigma_desvio, x_opt=None):
    limite = np.array(
        [[-2, 4],
        [-2, 5]]
    )

    def func(x1, x2):

        termo1 = np.exp(-(((x1**2)+(x2**2))))

        termo2 = 2*np.exp(-((x1-1.7)**2 + (x2-1.7)**2))

        return termo1 + termo2

    return classe(sigma_desvio, limite, func, x_array = x_opt)
def ex3(classe, sigma_desvio, x_opt=None):
    limite = np.array(
        [
            [-8, 8],
            [-8, 8]
        ]
    )

    def func(x1, x2):
        termo1 = -20 * np.exp(-0.2*np.sqrt(0.5*(x1**2+x2**2)))
        termo2 = - np.exp(0.5 * ( np.cos(2 * np.pi * x1) + np.cos( 2 * np.pi * x2)))
        return termo1 + termo2 + 20 + np.exp(1)
    
    return classe(sigma_desvio, limite, func, min = True, x_array = x_opt)

def ex4(classe, sigma_desvio, x_opt=None):
    limite = np.array(
        [
            [-5.12, 5.12],
            [-5.12, 5.12]
        ]
    )
    def func(x1, x2):
        term1 = (x1**2 - 10 * np.cos(2 * np.pi * x1) + 10)
        term2 = (x2**2 - 10 * np.cos(2 * np.pi * x2) + 10)
        return term1 + term2
    return classe(sigma_desvio, limite, func, min = True, x_array = x_opt)

def ex5(classe, sigma_desvio, x_opt=None):
    limite = np.array(
        [
            [-10, 10],
            [-10, 10]
        ]
    )
    def func(x1, x2):
        term1 = x1*np.cos(x1)/20
        term2 = 2 * np.exp(-(x1)**2 - (x2-1)**2) + 0.01*x1*x2
        return term1 + term2
    return classe(sigma_desvio, limite, func, x_array = x_opt)


def ex6(classe, sigma_desvio, x_opt=None):
    limite = np.array(
        [
            [-1, 3],
            [-1, 3]
        ]
    )
    def func(x1, x2):
        term1 = x1*np.sin(4*np.pi*x1)
        term2 = - x2 * np.sin(4*np.pi*x2 + np.pi) + 1
        return term1 + term2
    return classe(sigma_desvio, limite, func, x_array = x_opt)
    

def ex7(classe, sigma_desvio, x_opt=None):
    limite = np.array(
        [
            [0, np.pi],
            [0, np.pi]
        ]
    )
    def func(x1, x2):
        term1 = - np.sin(x1)* (np.sin((x1**2)/np.pi))**20
        term2 = - np.sin(x2) * (np.sin((2*x2**2)/np.pi))**20
        return term1 + term2
    return classe(sigma_desvio, limite, func, min = True, x_array = x_opt)

def ex8(classe,sigma_desvio, x_opt=None):
    limite = np.array(
        [
            [-200, 20],
            [-200, 20]
        ]
    )
    def func(x1, x2):
        term1 = - (x2 + 47) * np.sin(np.sqrt(np.abs(x1/2 + (x2 + 47))))
        term2 = - x1 * np.sin(np.sqrt(np.abs(x1 - (x2 + 47))))
        return term1 + term2
    return classe(sigma_desvio, limite, func, min = True, x_array = x_opt)
