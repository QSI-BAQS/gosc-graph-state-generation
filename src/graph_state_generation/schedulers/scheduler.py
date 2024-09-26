'''
    Scheduler base object
'''
import abc
import bisect
from graph_state_generation.graph_state import graph_state, graph_node
from graph_state_generation.mappers.mapper import Mapper


class Scheduler(abc.ABC):
    '''
        Scheduler base object
    '''
    def __init__(self,
                 graph: graph_state.GraphState,
                 mapper: Mapper,
                 *args,
                 **kwargs):
        '''
            scheduler base object
        '''
        self.graph = graph
        self.mapper = mapper
        self.schedule_layers = []


    def apply_mapper(self, node: graph_node.GraphNode) -> list:
        '''
            Applies the mapper to a graph node
        '''
        mapped_node = [self.mapper[i] for i in node]
        bisect.insort(mapped_node, node.qubit_idx)
        return mapped_node

    def __call__(self, *args, **kwargs):
        self.schedule(*args, **kwargs)

    @abc.abstractmethod
    def schedule(self, *args, **kwargs):
        '''
           Dispatch method for scheduler calls by concrete classes
        '''
