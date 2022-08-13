#!/usr/bin/python3
# ------------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# simple Graph class
# ------------------------------------------------------------
class Graph:
    def __init__(self, ordem):
        self.ordem = ordem
        self.MatrizAdjacencia = [[None for i in range(self.ordem)] for i in range(self.ordem)]
        self.tamanho = 0

    def verifica_len(self, A, B):
        X = A if A > B else B
        if X > self.ordem:
            index = 0
            while index < self.ordem:
                self.MatrizAdjacencia[index] += [None for k in range(X-self.ordem)]
                index += 1
            self.MatrizAdjacencia += [[None for i in range(X)] for k in range(X-self.ordem)]
            self.ordem = X
        return 0

    def adiciona_aresta(self, A, B, weight):
        self.verifica_len(A, B)
        self.MatrizAdjacencia[A-1][B-1] = weight
        self.tamanho += 1
        return 0

    def remove_aresta(self, A, B):
        if self.tamanho <= 0:
            return -1
        self.MatrizAdjacencia[A][B] = None
        self.tamanho -= 1
        return 0

    def tem_aresta(self, A, B):
        return self.MatrizAdjacencia[A][B] is None

    def grau_entrada(self, A):
        cont = 0
        for k in range(self.ordem):
            cont += 1 if self.MatrizAdjacencia[k][A] is not None else 0
        return cont

    def grau_saida(self, A):
        count = 0
        for k in range(self.ordem):
            count += 1 if self.MatrizAdjacencia[A][k] is not None else 0
        return count

    def grau(self, A):
        return self.grau_entrada(A)+self.grau_saida(A)

    def eh_denso(self):
        return self.tamanho > self.numero_maximo_arestas() *.9

    def numero_maximo_arestas(self):
        return (self.ordem-1)*self.ordem

    def imprime_matriz(self):
        print('\n===============\nMATRIZ\n')
        for index in range(self.ordem):
            print('{}: {}'.format(index, self.MatrizAdjacencia[index]))
        print('\n===============')
        return 0