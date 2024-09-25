'''
    Random Mapper
'''
import ctypes
import random

from graph_state_generation.mappers import mapper

class RandomMapper(mapper.Mapper):
    '''
        Random Mapper
    '''
    def mapping_fn(self, *args, **kwargs):
        '''
        mapper_fn
        Random Map
        '''
        self.map = list(map(ctypes.c_int32, random.sample(range(self.n_elements), self.n_elements)))
