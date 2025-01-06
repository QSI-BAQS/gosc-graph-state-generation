'''
    Random Mapper
'''
import ctypes
import random

from graph_state_generation.mappers import mapper
from graph_state_generation.mappers import linear_mapper
from graph_state_generation.mappers import comb_mapper

class BaseRandomMapper(mapper.Mapper):
    '''
        Random Mapper
    '''
    def mapping_fn(self, *args, **kwargs):
        '''
        mapper_fn
        Random Map
        '''
        self.map = list(map(ctypes.c_int32, random.sample(range(self.n_elements), self.n_elements)))


class LinearRandomMapper(linear_mapper.LinearMapper, BaseRandomMapper):
    '''
        Random Mapper
    '''
    def mapping_fn(self, *args, **kwargs):
        '''
        mapper_fn
        Random Map
        '''
        BaseRandomMapper.mapping_fn(self, *args, **kwargs)

class CombRandomMapper(comb_mapper.BaseCombMapper, BaseRandomMapper):
    '''
        Random Mapper
    '''
    def mapping_fn(self, *args, **kwargs):
        '''
        mapper_fn
        Random Map
        '''
        BaseRandomMapper.mapping_fn(self, *args, **kwargs)
