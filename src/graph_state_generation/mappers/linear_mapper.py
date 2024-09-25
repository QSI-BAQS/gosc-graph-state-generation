import ctypes
from mapper import Mapper

class LinearMapper(Mapper):

    def mapping_fn(self, *args, **kwargs): 
        '''
        mapper_fn
        Linear map
        '''
        for i in range(self.n_elements):
            self.map[i] = ctypes.c_int32(i)

