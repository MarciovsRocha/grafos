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


# -----------------------------------------------------------
# iter over dicts from list summing all values from dict keys
# return: int
def sum_list_dicts(some_list: list):
    s = 0
    for element in some_list:
        for key in element:
            s += element[key]
    return s


class Graph:
    """
        . : G R A P H : .

        * labeled: flag that indicates if graph will be labeled or not

        * directional: flag that indicates if graph will be directional or undirectional

        * weighted: flag that indicates if graph will have weights or not

        * self.AdjacencyList> represents the graph connections, 
                            this list starts empty by default

        * Connections: will be represented as tuples (A,B)

        * update: fluent pattern added to methods, that uses 'return 0'
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
            return self
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
        return self

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
        return self

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
        return self

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
        return self

    # -----------------------------------------------------------
    # returns lowest path between two nodes
    # return: [{node: accumulated_cost}]
    def dijkstra(self, source_node: str, target_node: str):
        if (source_node not in self.AdjacencyList) or (target_node not in self.AdjacencyList):
            print(
                'Não é possível verificar o menor caminho entre os vértices \'{}\' e \'{}\' pois um destes vértices não pertence ao grafo.'.format(
                    source_node, target_node))
            return -1
        current_node = source_node
        visited_nodes = [current_node]
        cost = [{str(current_node): 0}]
        while len(self.AdjacencyList) > len(visited_nodes):
            minor_child = None  # aux variable to determine the child with the lowest cost from current_node
            # iterate over adjacency list of current_node to find the lowest accumulated cost over child
            for node in self.AdjacencyList[current_node]:
                # if the child node is the target node compute the accumulated cost to him and
                # add into cost list and return the cost list
                if target_node == node:
                    cost.append({str(node): int(sum_list_dicts(cost)+self.AdjacencyList[current_node][node])})
                    return cost
                # if the child node is a non-visited node compute the accumulated cost to him
                # and adds him to the visited_nodes list
                if node not in visited_nodes:
                    visited_nodes.append(node)
                    acc_cost = sum_list_dicts(cost)+self.AdjacencyList[current_node][node]
                    # sets the minor child if its equals to None
                    if minor_child is None:
                        minor_child = (node, acc_cost)
                    else:  # update the minor child with the computed cost if its lower
                        minor_child = (node, acc_cost) if minor_child[1] < acc_cost else minor_child
            # with the minor_child selected, insert him into cost list
            # sets him as current_node
            cost.append({str(minor_child[0]): int(minor_child[1])})
            current_node = minor_child[0]
        print('The target node ({}) cannot be reachable from source node ({})'.format(target_node, source_node))
        return -1  # error, target node not reachable from source node
