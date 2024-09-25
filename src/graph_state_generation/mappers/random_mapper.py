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
    def mapping_fn(self, *args, rand=random.randint, **kwargs):
        '''
        mapper_fn
        Random Map
        '''
        self.map = list(map(ctypes.cint32, random.sample(range(self.n_elements), self.n_elements)))

