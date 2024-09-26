'''
    Base abstract mapper object
'''
import ctypes
import abc
from graph_state_generation.graph_state import graph_state

class Mapper(abc.ABC):
    '''
        Base abstract mapper object
    '''

    def __init__(self, graph: graph_state.GraphState, *args, **kwargs):
        '''
        Mapper Object
        '''
        n_elements = graph.n_vertices
        if n_elements > (1 << 32) - 2:
            raise IndexError("Map only supports up to 2**32 - 2 elements")

        if n_elements <= 0:
            raise IndexError("Map needs at least one element")

        self.graph = graph
        self.n_elements = n_elements
        self.map = (ctypes.c_int32 * self.n_elements)()
        self.mapping_fn(*args, **kwargs)

    @abc.abstractmethod
    def mapping_fn(self, *args, **kwargs):
        '''
            Abstract mapping function, called to create the map
        '''

    def __getitem__(self, idx: int):
        '''
            Wrapper to get an item from the map
        '''
        if idx > self.n_elements or idx < 0:
            raise IndexError()
    
        value = self.map[idx]

        if not isinstance(value, int):
            value = value.value 
        return value
 
    def __setitem__(self, idx: int, value: int):
        if idx > self.n_elements or idx < 0:
            raise IndexError()
        if isinstance(value, int):
            value = ctypes.c_int32(value)
        self.map[idx] = value 

    def __iter__(self):
        for i in range(self.n_elements):
            yield self[i]

    def __repr__(self):
        return ', '.join(i.__str__() for i in self.__iter__())

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return self.n_elements
