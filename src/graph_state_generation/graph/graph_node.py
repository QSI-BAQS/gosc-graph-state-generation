
class GraphNode:

    init_zero = object()
    init_plus = object()

    def __init__(self, init_state=None, adjacencies=None):
        if adjacencies is None:
            adjacencies = list()

        if init_state is None:
            init_state = GraphNode.init_zero

        self.init_state = init_state
        self.adjacencies = adjacencies

    def __getitem__(self, idx):
        return self.adjacencies[i] 

    def append(self, *args):
        self.adjacencies += args 

    def __iter__(self):
        return self.adjacencies.__iter__()

