#!/usr/bin/python3

# ------------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# simple Graph class
# ------------------------------------------------------------

from typing import Tuple


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
        self.AdjacencyList=[]
        self.labeled = labeled
        self.directional = directional
        self.weighted = weighted
    
    # ---------------------------------------------------------
    # adiciona o vertice 'A' ao grafo
    # return: None
    def adiciona_vertice(self, A: str):
        # code...
        print('method not implemented yet.')
        return -1
    
    # ----------------------------------------------------------
    # adiciona uma aresta com peso entre os vertices 'A' e 'B'
    # return: None
    def adiciona_aresta(self, A: str, B: str, weight: float = 1):
        # code...
        print('method not implemented yet.')
        return -1
    
    # ----------------------------------------------------------
    # remove aresta entre os vertices 'A' e 'B'
    # return: None
    def remove_aresta(self, A: str, B: str):
    # code...
        print('method not implemented yet.')
        return -1

    # ----------------------------------------------------------
    # remove o vertice 'A'
    # return: None
    def remove_vertice(self, A: str):
        # code...
        print('method not implemented yet.')
        return -1
    
    # ----------------------------------------------------------
    # verifica se existe uma aresta entre os vertices 'A' e 'B'
    # return: {x: bool}
    def tem_aresta(self, A: str, B: str):
        # code...
        print('method not implemented yet.')
        return -1

    # -----------------------------------------------------------
    # retorna a quantidade total de arestas conectadas (indegree+outdegree) 
    # do vertice 'A'
    # return: {x: int | x >= 0}
    def grau(self, A: str):
        # code...
        print('method not implemented yet.')
        return -1
    
    # -----------------------------------------------------------
    # retorna qual eh o peso da aresta entre os vertices 'A' e 'B'
    # return: {x: float | x >= 0}
    def peso(self, A: str, B: str):
        # code...
        print('method not implemented yet.')
        return -1

    # -----------------------------------------------------------
    # imprime a lista de adjacencias do grafo
    # return: None
    def imprime_lista_adjacencia(self):
        # code...
        print('method not implemented yet.')
        return -1    
