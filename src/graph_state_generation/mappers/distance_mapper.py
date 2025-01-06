'''
    Distance minimising mapper
'''
from graph_state_generation.mappers import random_mapper
from graph_state_generation.mappers import linear_mapper 
from graph_state_generation.mappers import comb_mapper

class BaseDistanceSortMapper(random_mapper.BaseRandomMapper):
    '''
        Weight sort Mapper
        Attempts to minimise the number of colliding stabilisers via bubble sort
    '''
    ALL_PASSES = object()

    def mapping_fn(self, *args, n_passes=1, **kwargs):
        '''
        mapper_fn
        Linear map
        '''
        random_mapper.BaseRandomMapper.mapping_fn(self)

        if n_passes == BaseDistanceSortMapper.ALL_PASSES:
            n_passes = self.n_elements

        for _ in range(n_passes):
            swapped = False
            for i, j in zip(range(self.n_elements), range(1, self.n_elements)):
                unswapped = self.pairwise_distance(i, j)
                self[i], self[j] = self[j], self[i]

                swapped = self.pairwise_distance(i, j)

                if swapped > unswapped:
                    self[i], self[j] = self[j], self[i]
                else:
                    swapped |= True

            # If no elements were swapped then break
            if not swapped:
                break

    def pairwise_distance(self, i, j):
        '''
            Calculates the intersections between two elements of the map
        '''
        return abs(self.position_x_group(i) - self.position_x_group(j))


    def graph_weight(self):
        '''
            Calculates the graph distance 
        '''
        weight = 0
        for i in range(self.n_elements):  # Ordered by current map
            for j in range(self.graph[i]):
                weight += self.pairwise_distance(i, j)
        return weight

class LinearDistanceSortMapper(linear_mapper.LinearMapper, BaseDistanceSortMapper):
    '''
        Dispatch class for namespace clarity
    '''
    pass

class CombDistanceSortMapper(comb_mapper.BaseCombMapper, BaseDistanceSortMapper):
    '''
        Dispatch class for namespace clarity
    '''
    def mapping_fn(self, *args, **kwargs): 
        BaseDistanceSortMapper.mapping_fn(self, *args, **kwargs) 
