from modelo.plot_board import plot_table as pt
from modelo.find_opt import Opt_colection
from modelo.temps import Temperatura_Simulada as ts
from modelo.funcoes_8_rainhas import *


tempora = ts(8, f, amostra, perturb(2))
bests = Opt_colection.get_bests(tempora)

pt.generate_gif(bests, "chesss_animation.gif")