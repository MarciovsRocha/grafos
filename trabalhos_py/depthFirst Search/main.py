#!/usr/bin/python3

# ------------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# ------------------------------------------------------------

from graph import Graph

G = Graph()
G.adiciona_vertice('marcio').\
    adiciona_vertice('mariana').\
    adiciona_vertice('anderson').\
    adiciona_vertice('arthur')
G.adiciona_aresta('marcio', 'mariana', 1).\
    adiciona_aresta('marcio', 'anderson', 3).\
    adiciona_aresta('mariana', 'arthur', 6).\
    adiciona_aresta('arthur', 'mariana', 10)

G.imprime_lista_adjacencia()

G.depth_first_search('marcio')