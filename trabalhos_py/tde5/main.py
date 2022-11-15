#!/usr/bin/python3

# ------------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# ------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from grafo_aleatorio import Grafo


G = Grafo(
    n_nodes=100,
    directional=True
)
print(G)

G.export_to_pajek()

graus = G.get_all_degrees(as_list=True)
for obj in G.get_highest_nodes():
    print(obj)

plt.hist(graus, edgecolor='black', alpha=.4)
plt.plot([np.mean(graus), np.mean(graus)], [0, 1500], r'--', label=f'Grau médio = {np.mean(graus)}')
plt.xlabel("Graus")
plt.ylabel("Frequência")
plt.legend()
plt.show()
