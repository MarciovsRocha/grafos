# ------------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# ------------------------------------------------------------
from grafo_aleatorio import Grafo
from utils import *

# ------------------------------------------------------
# some mocked data
SIMPLE_MOCK = 'dict_MOCK.json'
EXEMPLOS_SLIDE = 'exemplo_slide.json'
FIVE_HUNDRED_NODES = 'exported_graph_500_nodes.json'
BIG_ONE = 'big_one_nodes.json'


def feed_graph(graph: Grafo, option: str, n_nodes: int = 500, n_edges: int = 3):
    my_dict = {}
    if 'gaussian' == option.lower():
        graph.create_gaussian_distribution(n_nodes=n_nodes)
        return
    elif 'scale_free' == option.lower():
        graph.create_scale_free(n_nodes=n_nodes, n_edges=n_edges)
        return
    my_dict = load_json(option)
    graph.load_from_dict(my_dict)


G = Grafo(directional=True, verbose=True)
feed_graph(
    graph=G
    , option=EXEMPLOS_SLIDE
    , n_nodes=500
    , n_edges=3
)
# G.get_dag()

# G.export_to_json(FIVE_HUNDRED_NODES)
# G.import_from_pajek("output.net")
# G.export_to_pajek()
# G.degrees_histogram()
# G.get_strongly_connected_components()
# lowest = G.lowest_paths_histogram()
# for i in lowest:
#     line = ''
#     for j in lowest[i]:
#         line += f'{lowest[i][j]:<8}'
#     print(line)
G.get_central_node()
