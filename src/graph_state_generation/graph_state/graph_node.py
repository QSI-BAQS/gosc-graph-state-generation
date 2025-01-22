'''
    Graph node object
'''

import bisect
from itertools import chain


class GraphNode:
    '''
        Graph node object
    '''
    init_zero = object()
    init_plus = object()

    def __init__(self,
                 qubit_idx: int,
                 *args,
                 init_state=None,
                 adjacencies=None):
        '''
            Graph node object
        '''
        if adjacencies is None:
            adjacencies = []

        if init_state is None:
            init_state = GraphNode.init_zero

        self.qubit_idx = qubit_idx
        self.init_state = init_state
        self.adjacencies = list(args) + adjacencies
        adjacencies.sort()

    def __getitem__(self, idx: int) -> int:
        '''
            Gets the nth item from the adjacencies
        '''
        return self.adjacencies[idx]

    def append(self, *args):
        '''
            Appends edges to the node
        '''
        if isinstance(args[0], list):
            args = chain(*args)

        for i in args:
            bisect.insort(self.adjacencies, i)

    def remove(self, *idx):
        '''
            Removes elements from the adjacency matrix
            Assumes that the elements are still sorted
        '''
        for i in idx:
            self.adjacencies.pop(
                bisect.bisect_left(self.adjacencies, i)
            )

    def index(self, val):
        '''
            Proxies the index function over the adjacency list
        '''
        return self.adjacencies.index(val)

    def pop(self, val):
        '''
            Proxies the pop function over the adjacency list
        '''
        return self.adjacencies.pop(val)

    def __iter__(self):
        '''
            Iterates over the edges
        '''
        return self.adjacencies.__iter__()

    def __len__(self):
        return self.adjacencies.__len__()

    def __repr__(self):
        return f"{self.qubit_idx}: {self.adjacencies}"

    def flatten(self):
        return [self.qubit_idx] + self.adjacencies 
