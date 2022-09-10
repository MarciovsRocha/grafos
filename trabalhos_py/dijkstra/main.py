#!/usr/bin/python3

# ------------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# ------------------------------------------------------------

from graph import Graph

G = Graph()
G.adiciona_vertice('marcio')
G.adiciona_vertice('mariana')
G.adiciona_vertice('anderson')
G.adiciona_vertice('arthur')
G.adiciona_aresta('marcio', 'mariana', 1)
G.adiciona_aresta('marcio', 'anderson', 3)
G.adiciona_aresta('mariana', 'arthur', 6)
G.adiciona_aresta('arthur', 'mariana', 10)
G.remove_vertice('mariana')
G.imprime_lista_adjacencia()
