#!/usr/bin/python3
# ------------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# simple Graph class
# ------------------------------------------------------------

# -----------------------------------------------------------
# formata uma string passada para um output padrão de lista
# return: str
def limpar_string_lista(s):
    return s.replace('\'', '') \
        .replace('[', '') \
        .replace(']', '') \
        .replace(',', ' ') \
        .replace(';', ',')


class Graph:
    """
        . : G R A P H : .

        * labeled: flag that indicates if graph will be labeled or not

        * directional: flag that indicates if graph will be diretional or undirectional

        * weighted: flag that indicates if graph will have weights or not

        * self.AdjacencyList> represents the graph connections, 
                            this list starts empty by default

        * Connections: will be represented as tuples (A,B)                            
    """

    # 'constructor'
    def __init__(self, labeled: bool = True, directional: bool = True, weighted: bool = True):
        self.AdjacencyList = {}
        self.labeled = labeled
        self.directional = directional
        self.weighted = weighted

    # ---------------------------------------------------------
    # adiciona o vertice 'A' ao grafo
    # return: None
    def adiciona_vertice(self, A: str):
        if A not in self.AdjacencyList:
            self.AdjacencyList[A] = {}
            return 0
        else:
            print('já existe o vértice \'{}\' no grafo.')
            return -1

    # ----------------------------------------------------------
    # adiciona uma aresta com peso entre os vertices 'A' e 'B'
    # return: None
    def adiciona_aresta(self, A: str, B: str, weight: float = 1):
        if (A not in self.AdjacencyList) or (B not in self.AdjacencyList):
            print(
                'Não é possível criar uma aresta entre os vértices \'{}\' e \'{}\' pois um destes vértices não pertence ao grafo.'.format(
                    A, B))
            return -1
        if B in self.AdjacencyList[A]:
            print('Já existe uma aresta entre os vértices \'{}\' e \'{}\'.'.format(A, B))
            return -1
        self.AdjacencyList[A][B] = weight
        return 0

    # ----------------------------------------------------------
    # remove aresta entre os vertices 'A' e 'B'
    # return: None
    def remove_aresta(self, A: str, B: str):
        if (A not in self.AdjacencyList) or (B not in self.AdjacencyList):
            print(
                'Não é possível remover uma aresta entre os vértices \'{}\' e \'{}\' pois um destes vértices não pertence ao grafo.'.format(
                    A, B))
            return -1
        if B not in self.AdjacencyList[A]:
            print('Não existe uma aresta entre os vértices \'{}\' e \'{}\'.'.format(A, B))
            return -1
        self.AdjacencyList[A].pop(B)
        return 0

    # ----------------------------------------------------------
    # remove o vertice 'A'
    # return: None
    def remove_vertice(self, A: str):
        if A not in self.AdjacencyList:
            print('Não é possível remover o vértice \'{}\' pois este vértice não pertence ao grafo.'.format(A))
            return -1
        for key in self.AdjacencyList:
            if A in self.AdjacencyList[key]:
                self.AdjacencyList[key].pop(A)
        self.AdjacencyList.pop(A)
        return -1

    # ----------------------------------------------------------
    # verifica se existe uma aresta entre os vertices 'A' e 'B'
    # return: {x: bool}
    def tem_aresta(self, A: str, B: str):
        if (A not in self.AdjacencyList) or (B not in self.AdjacencyList):
            print(
                'Não é verificar uma aresta entre os vértices \'{}\' e \'{}\' pois um destes vértices não pertence ao grafo.'.format(
                    A, B))
            return -1
        return B in self.AdjacencyList[A]

    # -----------------------------------------------------------
    # retorna a quantidade total de arestas conectadas (indegree+outdegree) 
    # do vertice 'A'
    # return: {x: int | x >= 0}
    def grau(self, A: str):
        if A not in self.AdjacencyList:
            print('Não é verificar o grau do vértice \'{}\' pois este vértice não pertence ao grafo.'.format(A))
            return -1
        outdegree = len(self.AdjacencyList[A])
        indegree = 0
        for key in self.AdjacencyList:
            if A in self.AdjacencyList[key]:
                indegree += 1
        return indegree+outdegree

    # -----------------------------------------------------------
    # retorna qual eh o peso da aresta entre os vertices 'A' e 'B'
    # return: {x: float | x >= 0}
    def peso(self, A: str, B: str):
        if (A not in self.AdjacencyList) or (B not in self.AdjacencyList):
            print(
                'Não é possível verificar o peso de uma aresta entre os vértices \'{}\' e \'{}\' pois um destes vértices não pertence ao grafo.'.format(
                    A, B))
            return -1
        if B not in self.AdjacencyList[A]:
            print('Não existe uma aresta entre os vértices \'{}\' e \'{}\'.'.format(A, B))
            return -1
        return self.AdjacencyList[A][B]

    # -----------------------------------------------------------
    # imprime a lista de adjacencias do grafo
    # return: None
    def imprime_lista_adjacencia(self):
        for key in ['{}: {}'.format(
            A,
            ['({}; {}) ->'.format(B, self.AdjacencyList[A][B]) for B in self.AdjacencyList[A]]
        ) for A in self.AdjacencyList]:
            print(limpar_string_lista(key))
        return 0
