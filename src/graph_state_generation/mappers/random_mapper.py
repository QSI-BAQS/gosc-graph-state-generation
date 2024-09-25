'''
    Random Mapper
'''
import ctypes
import random

from mapper import Mapper

class RandomMapper(Mapper):
    '''
        Random Mapper
    '''
    def mapping_fn(self, *args, rand=random.randint, **kwargs):
        '''
        mapper_fn
        Random Map
        '''
        flag = ctypes.c_int32(-1)
        ctypes.memset(self.map, flag, 4 * self.n_elements)
        n_set = 0
        flag = int.from_bytes(flag, signed=True)
        # Not a good implementation,
        while n_set < self.n_elements:
            idx = rand(0, self.n_elements - 1)
            if self[idx] == flag:
                self[idx] = n_set
                n_set += 1
