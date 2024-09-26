'''
    Scheduler base object
'''
import abc
import copy
import bisect
from functools import reduce

from graph_state_generation.graph_state import graph_state, graph_node
from graph_state_generation.mappers.mapper import Mapper


class MappedNode:
    def __init__(self, graph_node, scheduler):  
        self.graph_node = graph_node
        self.scheduler = scheduler
        self.references = [] 
        self.mapped_values = self.scheduler.apply_mapper(self.graph_node)

    def build_references(self, ref_list):  
        self.references = [ref_list[i] for i in self.graph_node]   

    @property
    def qubit_idx(self):
        return self.graph_node.qubit_idx

    def remove_edge(self, idx): 
        edge_idx = self.graph_node.index(idx)
        self.references.pop(edge_idx)
       
        edge_idx = bisect.bisect_left(self.graph_node, idx) 
        self.graph_node.pop(edge_idx)
        self.mapped_values.pop(edge_idx)

    def __len__(self):
        return self.graph_node.__len__()

    def __repr__(self):
        return self.graph_node.__repr__()

    def __str__(self):
        return self.graph_node.__str__()

class Scheduler(abc.ABC):
    '''
        Scheduler base object
    '''
    def __init__(self,
                 graph: graph_state.GraphState,
                 mapper: Mapper,
                 *args,
                 MappedNode=MappedNode, 
                 **kwargs):
        '''
            scheduler base object
        '''
        self.graph = copy.deepcopy(graph)
        self.mapper = mapper
        self.schedule_layers = []
        self.mapped_segments = list(map(lambda x: MappedNode(x, self), self.graph))   
        reduce(lambda x, y: None, map(lambda x: MappedNode.build_references(x, self.mapped_segments), self.mapped_segments))   

    def apply_mapper(self, node: graph_node.GraphNode) -> list:
        '''
            Applies the mapper to a graph node
        '''
        mapped_node = [self.mapper[i] for i in node]
        mapped_node.append(self.mapper[node.qubit_idx])
        return mapped_node

    def __call__(self, *args, **kwargs):
        self.schedule(*args, **kwargs)

    def __len__(self):
        return self.schedule_layers.__len__()
    
    @abc.abstractmethod
    def schedule(self, *args, **kwargs):
        '''
           Dispatch method for scheduler calls by concrete classes
        '''



