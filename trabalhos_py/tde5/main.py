# ------------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# ------------------------------------------------------------
import numpy as np
#import matplotlib.pyplot as plt
from grafo_aleatorio import Grafo
from  utils import *


G = Grafo(directional=True, verbose=True)
G.create_scale_free(n_nodes=10000, n_edges=3)
#G.create_gaussian_distribution(n_nodes=10)
#meu_dict = load_json('dict_MOCK.json')
#G.load_from_dict(meu_dict)
G.export_to_json('big_one_nodes.json')
#G.import_from_pajek("output.net")

#G.export_to_pajek()

#print(G)

#graus = G.get_all_degrees(as_list=True)
#for obj in G.get_highest_nodes():
   #print(obj)

#plt.hist(graus, edgecolor='black', alpha=.4)
#plt.plot([np.mean(graus), np.mean(graus)], [0, 1500], r'--', label=f'Grau médio = {np.mean(graus)}')
#plt.xlabel("Graus")
#plt.ylabel("Frequência")
#plt.legend()
#plt.show()

#G.get_strongly_connected_components()
