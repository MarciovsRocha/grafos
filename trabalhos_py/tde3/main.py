#!/usr/bin/python3

# ------------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# ------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# # import section
from graph import Graph
import extract as ex
import os
import json

# ---------------------------------------------------------------------------------------------------------------------
# constants section
nodes_file = 'nodes.json'
nodes = None
Q = ('--'*40)+'\n\n'# "quebra de sessão" no console
n = 20  # elementos a serem printados
d = 5  # "saltos" para procurar nos alcancaveis

# ---------------------------------------------------------------------------------------------------------------------
# instance section

# creates new graph
G = Graph()

# initiates the instance of emails_list
file_list = ex.list_files('./dataset/')
if 'nodes.json' not in os.listdir(os.curdir):
    nodes = ex.mount_objects(file_list)
    nodes = json.dumps(nodes, indent=4, sort_keys=False, ensure_ascii=False)
    # export nodes to a file named 'nodes.json'
    with open(nodes_file, 'w', encoding='utf-8') as f:
        f.write(nodes)
        f.close()
else:  # loads json from file
    with open(nodes_file, 'r') as f:
        nodes = f.read()
        f.close()

# verifica se deve transformar para um objeto dict
if (dict != type(nodes)) and (str == type(nodes)):
    nodes = json.loads(nodes)

# ---------------------------------------------------------------------------------------------------------------------
# poppulating graph

for A in nodes:
    if not G.existe_vertice(A):
        G.adiciona_vertice(A)
    for B in nodes[A]:
        _weight = nodes[A][B]
        if not G.existe_vertice(B):
            G.adiciona_vertice(B)
        # se ja existe a aresta, só atualiza o peso
        if G.tem_aresta(A, B):
            G.AdjacencyList[A][B] += _weight
        else:
            G.adiciona_aresta(A, B, _weight)


# ---------------------------------------------------------------------------------------------------------------------
#G.imprime_lista_adjacencia()

# Orderm do Grafo
print('{}Orderm do Grafo(número de vértices): {}'.format(Q, G.ordem()))

# Número de arestas do grafo
print('{}Número de arestas do grafo: {}'.format(Q, G.arestas()))

# Individuos com maior outdegree
msg = ''
for element in G.n_individuos_outdegree(n):
    msg += '{}: {}\n'.format(element['name'], element['value'])
print('{}{} Individuos com maior outdegree: {}'.format(Q, n, msg))

# Individuos com maior indegree
msg = ''
for element in G.n_individuos_indegree(n):
    msg += '{}: {}\n'.format(element['name'], element['value'])
print('{}{} Individuos com maior indegree: {}'.format(Q, n, msg))

# Grafo é euleriano
print('{} Grafo é euleriano: {}'.format(Q, G.is_eulerian()))

# Busca em profundidade
busca, tempo = G.deepth_search('danielle.marcinkowski@enron.com', 'andrew.wu@enron.com')
print('{} Busca em profundidade(danielle.marcinkowski@enron.com -> andrew.wu@enron.com):\n    lista: {}\n    tempo de busca: {}'.format(
    Q
    , busca[:3]
    , tempo
))

# Busca em largura
busca, tempo = G.breadth_search('danielle.marcinkowski@enron.com', 'andrew.wu@enron.com')
print('{} Busca em largura(danielle.marcinkowski@enron.com -> andrew.wu@enron.com):\n    lista: {}\n    tempo de busca: {}'.format(
    Q
    , busca[:3]
    , tempo
))

# Nós anlcançaveis
print('{}Busca de nós alcancaveis a uma distancia D({}):\nmostra somente os 3 primeiros elementos da lissta + último\n\n'.format(Q, d))
busca = G.reachable_nodes('danielle.marcinkowski@enron.com', d)
for jump in busca:
    print('  - Nós com total de {} salto(s): '.format(jump), end='')
    for node in busca[jump][:3]:
        print('{}'.format(node), end='; ')
    print('...; {}\n'.format(busca[jump][len(busca[jump])-1]))
