'''
    Scheduler base object
'''
import abc
import copy
import bisect
from functools import reduce

from graph_state_generation.graph_state.graph_state import GraphState
from graph_state_generation.graph_state.graph_node import GraphNode
from graph_state_generation.mappers.mapper import Mapper


class MappedNode:
    '''
        MappedNode object
        Joins a mapping and a graph vertex
    '''
    def __init__(self, graph_node, scheduler):
        self.graph_node = graph_node
        self.scheduler = scheduler
        self.references = []
        self.mapped_values = self.scheduler.apply_mapper(self.graph_node)

    def build_references(self, ref_list):
        '''
            Constructs a list of references to other mapped nodes
        '''
        self.references = [ref_list[i] for i in self.graph_node]

    @property
    def qubit_idx(self):
        '''
            Returns the circuit qubit index of this node
        '''
        return self.graph_node.qubit_idx

    def remove_edge(self, idx):
        '''
            Removes the edge to circuit qubit idx from this node
        '''
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
                 graph: GraphState,
                 mapper: Mapper,
                 *args,
                 mapped_node=MappedNode,
                 call_scheduler=True,
                 **kwargs):
        '''
            scheduler base object
        '''
        self.graph = copy.deepcopy(graph)
        self.mapper = mapper
        self.called = False
        self.schedule_layers = []
        self.mapped_segments = list(map(lambda x: mapped_node(x, self), self.graph))
        reduce(
            lambda x, y: None,
            map(
                lambda x: mapped_node.build_references(x, self.mapped_segments),
                self.mapped_segments
            )
        )
        if call_scheduler:
            self.schedule()
            self.called = True

    def apply_mapper(self, node: GraphNode) -> list:
        '''
            Applies the mapper to a graph node
        '''
        mapped_node = [self.mapper[i] for i in node]
        mapped_node.append(self.mapper[node.qubit_idx])
        return mapped_node

    def __call__(self, *args, **kwargs):
        self.schedule(*args, **kwargs)
        self.called = True

    def __len__(self):
        return self.schedule_layers.__len__()

    @abc.abstractmethod
    def schedule(self, *args, **kwargs):
        '''
           Dispatch method for scheduler calls by concrete classes
        '''
