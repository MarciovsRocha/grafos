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

    # -----------------------------------------------------------
    # verifica se exite um vértice no grafo
    # return: bool
    def existe_vertice(self, A: str = ''):
        return ('' != A) and (A in self.AdjacencyList)

    # -----------------------------------------------------------
    # retorna a ordem do grafo (numero de vertices)
    # return: int
    def ordem(self):
        return len(self.AdjacencyList)

    # -----------------------------------------------------------
    # retorna o número de arestas do grafo
    # return: int
    def arestas(self):
        arestas = 0
        for node in self.AdjacencyList:
            arestas += self.grau(node)
        return arestas

    # -----------------------------------------------------------
    # retorna o n-indivíduos com maior grau de saída
    # e o valor correspondente
    # return: {individuo: outdegree}
    def n_individuos_outdegree(self, n: int = 5):
        from bst import BinarySearchTree, Node
        bst = BinarySearchTree()
        for A in self.AdjacencyList:
            bst.add_node(Node(name=A, value=len(self.AdjacencyList[A])))
        higher_nodes = [{'name': current_node.name, 'value': current_node.value} for current_node in bst.list_higher_nodes(n)]
        return higher_nodes

    # -----------------------------------------------------------
    # retorna o n-indivíduos com maior grau de entrada
    # e o valor correspondente
    # return: {individuo: outdegree}
    def n_individuos_indegree(self, n: int = 5):
        from bst import BinarySearchTree, Node
        bst = BinarySearchTree()
        for A in self.AdjacencyList:
            # calcula o grau de entrada
            indegree = 0
            for key in self.AdjacencyList:
                if A in self.AdjacencyList[key]:
                    indegree += 1

            bst.add_node(Node(name=A, value=indegree))
        higher_nodes = [{'name': current_node.name, 'value': current_node.value} for current_node in bst.list_higher_nodes(n)]
        return higher_nodes

    # -----------------------------------------------------------
    # verifica se o grafo é euleriano
    # return: bool (True | False)
    def is_eulerian(self):
        eulerian = True
        for A in self.AdjacencyList:
            eulerian = eulerian and (0 == (self.grau(A) % 2))
        return eulerian

    # -----------------------------------------------------------
    # verifica alcancabilidade por profundidade
    # do elemento A ao B
    # return: bool (True | False)
    def deepth_search(self, A: str = '', B: str = ''):
        visited_nodes = []
        stack=[A]
        import time
        start = time.time()
        while 0 < len(stack):
            current_node = stack.pop()
            if current_node not in visited_nodes:
                visited_nodes.append(current_node)
            for node in self.AdjacencyList[current_node]:
                if node not in visited_nodes:
                    stack.append(node)
                if B == node:
                    return visited_nodes, (time.time()-start)
        return visited_nodes, (time.time()-start)

    # -----------------------------------------------------------
    # verifica alcancabilidade por largura
    # do elemento A ao B
    # return: bool (True | False)
    def breadth_search(self, A: str = '', B: str = ''):
        visited_nodes = []
        stack = [A]
        import time
        start = time.time()
        while (0 < len(stack)) and (len(self.AdjacencyList) > len(visited_nodes)):
            current_node = stack.pop()
            visited_nodes.append(current_node)
            if B == current_node:
                return visited_nodes, (time.time() - start)
            for node in self.AdjacencyList[current_node]:
                if node not in visited_nodes:
                    stack.append(node)
        return visited_nodes, (time.time() - start)

    # -----------------------------------------------------------
    # verifica todos os nodes alcancaveis dentro do limite
    # return: dict {jump: list}
    def reachable_nodes(self, A: str = '', n: int = 1):
        visited_nodes = []
        reachable = {'1': [k for k in self.AdjacencyList[A]]}
        for i in range(2, (n+1)):
            stack = str(i-1)
            if stack in reachable:
                for node in reachable[stack]:
                    if node not in visited_nodes:
                        visited_nodes.append(node)
                        r = [k for k in self.AdjacencyList[node]]
                        for n in r:
                            if n in visited_nodes:
                                r.remove(n)
                        if str(i) not in reachable:
                            reachable[str(i)] = r
                        else:
                            reachable[str(i)] += r
        return reachable
