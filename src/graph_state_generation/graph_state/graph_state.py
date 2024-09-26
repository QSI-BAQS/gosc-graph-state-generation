'''
    Graph State Object
'''
from graph_state_generation.graph_state import graph_node
from graph_state_generation.visualization_tools import graph_to_tikz


class GraphState:
    '''
        Graph State Object
    '''

    def __init__(self, n_vertices: int):

        self.n_vertices = n_vertices
        self.vertices = [
                graph_node.GraphNode(i) for i in range(self.n_vertices)
            ]

    def __getitem__(self, idx: int):
        '''
        '''
        return self.vertices[idx]

    def __iter__(self):
        return self.vertices.__iter__()

    def __repr__(self):
        return ', '.join(map(str, self.vertices))

    def __len__(self):
        return self.n_vertices

    def append(self, idx: int, jdx: int):
        '''
            Adds an adjacency between nodes idx and jdx
        '''
        self[idx].append(jdx)
        self[jdx].append(idx)

    def tikz(self):
        '''
            Creates a tikz depiction of the graph
        '''
        return graph_to_tikz.graph_to_tikz(self)
