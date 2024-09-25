import abc
import bisect

class Scheduler(abc.ABC):
    def __init__(self, graph, mapper):
        self.graph = graph
        self.mapper = mapper
        self.schedule_layers = []


    def apply_mapper(self, graph_node):
        mapped_graph_node = [self.mapper[i] for i in graph_node]
        bisect.insort(mapped_graph_node, graph_node.qubit_idx)
        return mapped_graph_node
        

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        pass
