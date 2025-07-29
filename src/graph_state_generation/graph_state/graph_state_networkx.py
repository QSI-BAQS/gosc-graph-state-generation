'''
    Graph State Object
    Implemented using the networkx backend
'''
import networkx as nx

from graph_state_generation.graph_state import graph_node
from graph_state_generation.graph_state.graph_state import GraphState_

from graph_state_generation.visualization_tools import graph_to_tikz


class GraphStateNetworkx(GraphState):
    '''
        Graph State Object
    '''

    def __init__(self, n_vertices: int):

        self.n_vertices = n_vertices
        self.graph = nx.graph.Graph() 
        for i in range(n_vertices):
            self.graph.add_node(i) 

    def __getitem__(self, idx: int):
        '''
        '''
        edges = [i for i in self.graph.edges if idx in i]
        return edges 

    def __iter__(self):
        return self.graph.__iter__()

    def __repr__(self):
        return ', '.join(map(str, self.__iter__())

    def __len__(self):
        return self.n_vertices

    def append(self, idx: int, jdx: int):
        '''
            Adds an adjacency between nodes idx and jdx
        '''
        self.graph.add_edge(idx, jdx)

    def pop(self, *idx):
        '''
            Proxies a pop operation on the vertices
        '''
        self.g.remove_nodes_from(idx)
        self.n_vertices = len(self.graph)

    def tikz(self):
        '''
            Creates a tikz depiction of the graph
        '''
        return graph_to_tikz.graph_to_tikz(self)
