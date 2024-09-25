'''
    Graph State Object
'''

from graph_state_generation.graph_state import graph_node

class GraphState:
    '''
        Graph State Object
    '''

    def __init__(self, n_vertices):

        self.n_vertices = n_vertices
        self.vertices = [graph_node.GraphNode(i) for i in range(self.n_vertices)]

    def __getitem__(self, idx):
        '''
        '''
        return self.vertices[idx]

    def __iter__(self):
        return self.vertices.__iter__()

    def __repr__(self):
        return ', '.join(map(str, self.vertices))

    def append(self, idx : int, jdx : int):
        '''
            Adds an adjacency between nodes idx and jdx 
        '''
        self[idx].append(jdx)
        self[jdx].append(idx)
