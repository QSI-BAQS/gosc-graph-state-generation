'''
    Linear Mapper
'''
import ctypes
from graph_state_generation.mappers import random_mapper 


class WeightSortMapper(random_mapper.RandomMapper):
    '''
        Linear Mapper
        Maps qubit i to position i
    '''
    ALL_PASSES=object()

    def mapping_fn(self, *args, n_passes=1, **kwargs):
        '''
        mapper_fn
        Linear map
        '''
        super().mapping_fn()

        if n_passes == WeightSortMapper.ALL_PASSES:
            n_passes = self.n_elements

        for _ in range(n_passes):
           for i, j in zip(range(self.n_elements), range(1, self.n_elements)): 
                unswapped = self.pairwise_graph_weight(i, j)
                tmp = self[j] 
                self[j] = self[i] 
                self[i] = tmp 

                swapped = self.pairwise_graph_weight(i, j)

                if swapped > unswapped:
                    tmp = self[j] 
                    self[j] = self[i] 
                    self[i] = tmp 

    def pairwise_graph_weight(self, i, j):
        if self[i] > self[j]: 
            tmp = j
            j = i
            i = tmp

        pairwise_weight = 0
        for edges_i in self.graph[i]:  
            for edges_j in self.graph[j]:  
                if self[edges_i] > self[edges_j]:
                    pairwise_weight += 1
        return pairwise_weight



    def graph_weight(self):
        weight = 0
        for i in range(self.n_elements): # Ordered by current map
            stab_lower = self.graph[i] 
            for stab_upper in self.graph[i + 1:]:
                for edge_lower in stab_lower:
                    for edge_upper in stab_upper:
                        if (self[edge_lower] > self[edge_upper]): 
                                weight += 1
        return weight
                    
