'''
    Scheduler base object
'''
import abc
import bisect

class Scheduler(abc.ABC):
    '''
        Scheduler base object
    '''
    def __init__(self, graph, mapper):
        '''
            scheduler base object
        '''
        self.graph = graph
        self.mapper = mapper
        self.schedule_layers = []

    def apply_mapper(self, graph_node) -> list:
        '''
            Applies the mapper to a graph node
        '''
        mapped_graph_node = [self.mapper[i] for i in graph_node]
        bisect.insort(mapped_graph_node, graph_node.qubit_idx)
        return mapped_graph_node

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        pass
