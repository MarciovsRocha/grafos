# ---------------------------------------------------------
# import section
#import pandas as pd
from random import random
from bst import BinarySearchTree, Node
#from pajek_tools import PajekWriter
from utils import *

# ---------------------------------------------------------
# constants section

MIN_NODES = 10000
MIN_EDGES = 15000


# ---------------------------------------------------------
# graph class
# USE FLUENT NOTATION
class Grafo:
    """
        . : G R A P H : .

        * directional: flag that indicates if graph will be directional or undirectional

        * weighted: flag that indicates if graph will have weights or not

        * self.AdjacencyList> represents the graph connections,
                            this list starts empty by default

        * Connections: will be represented as tuples (A,B)
    """

    # private attributes
    __directional: bool
    __adjacency_list: dict
    # this prob value will generate nodes with more edges than others
    # and n-edges will follow a gaussian distribution
    __connection_prob: float
    __max_degree: int
    __min_degree: int
    __nodes_data: dict

    # public attributes
    size: int
    order: int
    VERBOSE: bool

    # ---------------------------------------------------------
    # constructor
    def __init__(self , directional: bool = True, conn_prob: float = (2/3), verbose: bool = False):
        self.__directional = directional
        self.__adjacency_list = {}
        self.__connection_prob = conn_prob
        self.__max_degree = 0
        self.__min_degree = 0
        self.__nodes_data = {}
        self.size = 0
        self.order = 0
        self.VERBOSE = verbose

    # ---------------------------------------------------------
    # custom printable object
    def __str__(self):
        return f'O Grafo aleatorio possui {self.order} vértices e {self.size} arestas.'

    # ---------------------------------------------------------
    # insert new node into graph with available name in Users.txt
    def new_node(self, node_name: str = ''):
        node_name = new_name() if '' == node_name else node_name
        if node_name in self.__adjacency_list:
            raise Exception(f'The node "{node_name}" already exists in graph.')
        self.__adjacency_list[node_name] = {}
        if self.__directional:
            self.__nodes_data[node_name] = {'outdegree': 0, 'indegree': 0}
        else:
            self.__nodes_data[node_name] = {'degree': 0}
        self.order += 1
        return self

    # ---------------------------------------------------------
    # return number of indegree of specified node
    def node_indegree(self, A):
        self.__valida_nodes(A)
        return self.__nodes_data[A]['indegree']

    # ---------------------------------------------------------
    # return number of outdegree of specified node
    def node_outdegree(self , A):
        self.__valida_nodes(A)
        return self.__nodes_data[A]['outdegree']

    # ---------------------------------------------------------
    # return number of indegree + outdegree of specified node
    def node_degree(self, A):
        if self.__directional:
            return self.__nodes_data[A]['outdegree'] + self.__nodes_data[A]['indegree']
        return self.__nodes_data[A]['degree']

    # ---------------------------------------------------------
    # return dict or list of degrees
    # list doesnt grant order or index
    # dict grant degree of each node (node_label = dict_key)
    def get_all_degrees(self, as_list: bool = False):
        if as_list:
            return [self.node_degree(node) for node in self.__adjacency_list]
        degrees = {}
        for node in self.__nodes_data:
            degrees[node] = self.node_degree(node)
        return degrees

    # ---------------------------------------------------------
    # insert new edge between two nodes
    # if already exists overwrite the old value with the new value
    def new_edge(self, A, B, weight):
        self.__valida_nodes(nodes=[A, B])
        if A == B:
            raise Exception(f'Nodes "{A}" and "{B}" are the same.')
        if self.__directional:
            self.__adjacency_list[A][B] = weight
            self.__nodes_data[A]['outdegree'] += 1
            self.__nodes_data[B]['indegree'] += 1
        else:
            self.__adjacency_list[A][B] = weight
            self.__adjacency_list[B][A] = weight
            self.__nodes_data[A]['degree'] += 1
            self.__nodes_data[B]['degree'] += 1
        self.size += 1
        # adjust variables MIN MAX
        degrees_list = self.get_all_degrees(as_list=True)
        self.__max_degree = max(degrees_list)
        self.__min_degree = min(degrees_list)
        return self

    # ---------------------------------------------------------
    # creates an initial graph with 1k nodes and max 150 edges per node
    # ONLY FOR DEBUGGING
    def get_highest_nodes(self, n: int = 10):
        bst = BinarySearchTree()
        for node in self.__adjacency_list:
            bst.add_node(Node(value=self.node_degree(node), name=node))
        return [f'{node.name}: {node.value}' for node in bst.list_higher_nodes(n=n)]

    # ---------------------------------------------------------
    # Exports the graph to Pajek file format
    def export_to_pajek(self):
        data = []
        for A in self.__adjacency_list:
            for B in self.__adjacency_list[A]:
                if A != B:
                    data.append([A, B, self.__adjacency_list[A][B]])

#        df = pd.DataFrame(data, columns=["source", "target", "weight"])
#        writer = PajekWriter(df,
#                             directed=True,
#                             citing_colname="source",
#                             cited_colname="target",
#                             weighted=True)
#        writer.write("output.net")
        return self

    def import_from_pajek(self, path):
        graph = {}
        name_index = [0]
        nodes_remaining = -1
        file = open(path, 'r')
        for data in self.clean_generator(file):
            for row in data:
                if row[0] == "*Vertices":
                    nodes_remaining = int(row[1])
                elif nodes_remaining > 0:
                    graph[row[1][1:-1]] = {}
                    name_index.append(row[1][1:-1])
                    nodes_remaining -= 1
                elif row[0] != "*Arcs":
                    graph[name_index[int(row[0])]][name_index[int(row[1])]] = int(row[2])
        self.load_from_dict(graph)


    def clean_generator(self, fhandler): yield (row.strip().split() for row in fhandler)

    # ---------------------------------------------------------
    # verify if all passed nodes exists in graph
    def __valida_nodes(self, nodes):
        if list == type(nodes):
            if not exists_nodes(nodes, [A for A in self.__adjacency_list]):
                raise Exception(f'One or more nodes doesnt exists in graph.')
        if str == type(nodes):
            if not exists_nodes([nodes], [A for A in self.__adjacency_list]):
                raise Exception(f'Node "{nodes}" doesnt exists in graph.')
        return self

    # ---------------------------------------------------------
    # create graph with gaussian distribution of edges
    def create_gaussian_distribution(self, n_nodes : int):
        # creates initial nodes
        if self.VERBOSE:
            print(f'Criando nodes inicias.')
        while 0 < n_nodes:
            self.new_node()
            n_nodes -= 1
        # create initial edges
        if self.VERBOSE:
            print(f'Criando lista de adjacencias Gaussiana.')
        for A in self.__adjacency_list:
            for B in self.__adjacency_list:
                if (A != B) and (random() > self.__connection_prob):
                    self.new_edge(A , B , new_weight())
        return self

    # ---------------------------------------------------------
    # create scale free graph
    def create_scale_free(self, n_nodes: int, n_edges: int):
        initial_nodes = int(n_nodes / 15)
        n_nodes = n_nodes-initial_nodes
        self.create_gaussian_distribution(n_nodes=initial_nodes)
        # this function will create a scale-free graph
        new_nodes = []
        # creates initial nodes
        if self.VERBOSE:
            print(f'Criando nodes inicias.')
        while n_nodes > len(new_nodes):
            new_nodes.append(new_name())
            self.new_node(new_nodes[len(new_nodes) - 1])
        # create k-edges for each new_node
        if self.VERBOSE:
            nodes = list(self.__adjacency_list.keys())
        for A in new_nodes:
            if self.VERBOSE:                
                print(f'Criando arestas para o node: #{(nodes.index(A)+1)} - {A}.')
            while n_edges > self.node_degree(A):
                for B in self.__adjacency_list:
                    if n_edges < self.node_degree(A):
                        break
                    # (nodes not equal)(rand * B_degree > prob)
                    if A != B:
                        b_conn_prob = random() * min_max(MIN=self.__min_degree , MAX=self.__max_degree ,
                                                         x=self.node_degree(B))
                        if b_conn_prob > self.__connection_prob:
                            self.new_edge(A , B , new_weight())
                            print(f'Criada aresta #{self.node_degree(A)} para o node: #{(nodes.index(A)+1)} - {A}.')
        return self

    # ---------------------------------------------------------
    # loads data from dict python that has the same
    # architecture that adjacency list
    def load_from_dict(self, grafo: dict):
        msg = 'Import dict not compatible with architecture.'
        added_nodes = []  # [A, B]
        added_edges = []  # (A, B)
        try:
            for A in grafo:
                # verify structure
                if type(grafo[A]) != dict:
                    raise Exception(msg)
                # verify if already exists
                if A not in self.__adjacency_list:
                    added_nodes.append(A)
                    self.new_node(A)
                for B in grafo[A]:
                    # verify if already exists
                    if B not in self.__adjacency_list:
                        added_nodes.append(B)
                        self.new_node(B)
                    # verify structure
                    if type(grafo[A][B]) != int:
                        raise Exception(msg)
                    self.new_edge(A , B , grafo[A][B])
                    added_edges.append((A, B))
        except Exception as e:
            # rollback changes
            for edge in added_edges:
                self.__adjacency_list[edge[0]].pop(edge[1])
            for node in added_nodes:
                if node in self.__adjacency_list:
                    self.__adjacency_list.pop(node)
            raise e
        return self

    # ---------------------------------------------------------
    # returns number of components of graph
    # size + order (n_edges + n_nodes)
    def get_components(self):
        return self.size + self.order

    # ---------------------------------------------------------
    # returns transpose graph
    def get_graph_transpose(self):
        transposed_graph = {index: {} for index in self.__adjacency_list}
        for a in self.__adjacency_list:
            for b in self.__adjacency_list[a]:
                val = self.__adjacency_list[a][b]
                transposed_graph[b][a] = val
        return transposed_graph

    # ---------------------------------------------------------
    # executes DFS and returns visited nodes and leafs
    def dfs_visit_finish(self, visited_nodes: list, finished_nodes: list, node,  graph):
        visited_nodes.append(node)
        for b in graph[node]:
            if b not in visited_nodes:
                visited_nodes, finished_nodes = self.dfs_visit_finish(visited_nodes, finished_nodes, b, graph)
        finished_nodes.append(node)
        return visited_nodes, finished_nodes

    # ---------------------------------------------------------
    # returns sub-graphs that represents strongy connected nodes
    # of original graph
    def get_strongly_connected_components(self):
        visited_nodes = []
        finished_nodes = []
        scc = []
        order = []

        for a in self.__adjacency_list:
            if a not in visited_nodes:
                visited_nodes, finished_nodes = self.dfs_visit_finish(visited_nodes, finished_nodes, a,
                                                                      self.__adjacency_list)

        graph_transpose = self.get_graph_transpose()
        finished_nodes = finished_nodes[::-1]
        visited_nodes = []
        finish = []

        for a in finished_nodes:
            if a not in visited_nodes:
                order.append(a)
                visited_nodes, finish = self.dfs_visit_finish(visited_nodes, finish, a, graph_transpose)

        cont = -1

        for a in finished_nodes:
            if a in order:
                scc.append([])
                cont += 1
            scc[cont].append(a)

        return {"num_scc": len(scc), "scc_list": scc}

    # ---------------------------------------------------------
    # exports the graph to json file
    def export_to_json(self, file_name: str = 'exported_graph.json'):
        if '' != file_name:
            with open(file_name, 'w') as file:
                file.write(json.dumps(self.__adjacency_list, indent=4, ensure_ascii=True))
            print(f'Grafo exportado para o arquivo: {file_name} com sucesso.')

    # ---------------------------------------------------------
    # returns DAG from actual graph
    def get_dag(self):
        DAG = {}
        # realize DFS
        visited_nodes = []
        finished_nodes = []
        for A in self.__adjacency_list:
            if A not in visited_nodes:
                visited_nodes, finished_nodes = self.dfs_visit_finish(visited_nodes, finished_nodes, A, self.__adjacency_list)
        # finished_nodes = stack topological_sort  backwards
        for node in finished_nodes[::-1]:
            DAG[node] = {}
            for conn in self.__adjacency_list[node]:
                if conn not in DAG:
                    DAG[node][conn] = self.__adjacency_list[node][conn]
        return DAG
