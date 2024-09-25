import ctypes
import abc

class Mapper(abc.ABC):
    def __init__(self, n_elements : int, *args, **kwargs):
        '''
        Mapper Object
        ''' 
        if n_elements > (1 << 32) - 2:
            raise IndexError("Map only supports up to 2**32 - 2 elements")

        if n_elements <= 0:
            raise IndexError("Map needs at least one element")

        self.n_elements = n_elements
        self.map = (ctypes.c_int32 * self.n_elements)() 
        self.mapping_fn(*args, **kwargs)        

    def __getitem__(self, idx:int) -> ctypes.c_int32:
        '''
            Wrapper to get an item from the map
        '''
        if idx > self.n_elements or idx < 0:
            raise IndexError()
        return self.map[idx]

    def __setitem__(self, idx:int, value:int): 
        if idx > self.n_elements or idx < 0:
            raise IndexError()
        self.map[idx] = ctypes.c_int32(value)

    def __iter__(self):
        for i in range(self.n_elements):  
            yield self.map[i]

    def __repr__(self):
        return ', '.join(i.__str__() for i in self.__iter__()) 

    def __str__(self):
        return self.__repr__()
