'''
    Linear Mapper
'''
import ctypes
from graph_state_generation.mappers import mapper

class LinearMapper(mapper.Mapper):
    '''
        Linear Mapper
        Maps qubit i to position i
    '''
    def mapping_fn(self, *args, **kwargs):
        '''
        mapper_fn
        Linear map
        '''
        for i in range(self.n_elements):
            self.map[i] = ctypes.c_int32(i)
