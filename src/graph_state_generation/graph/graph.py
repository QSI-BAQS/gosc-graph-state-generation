'''
    Graph Object
'''

from graph_node import GraphNode

class Graph: 
    def __init__(self, n_vertices):

        self.n_vertices = n_vertices
        self.vertices = [GraphNode() for i in self.n_vertices]

    def __getitem__(self, idx):
        '''
        '''
        return self.vertices[idx]

    def __iter__(self):
        return self.vertices.__iter__()

    def __repr__(self):
        return ', '.join(map(str, self.vertices))
