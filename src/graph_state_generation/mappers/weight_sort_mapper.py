'''
    Linear Mapper
'''
from graph_state_generation.mappers import random_mapper
from graph_state_generation.mappers import comb_mapper


class BaseWeightSortMapper(random_mapper.BaseRandomMapper):
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

        if n_passes == BaseWeightSortMapper.ALL_PASSES:
            n_passes = self.n_elements

        for _ in range(n_passes):
            swapped = False
            for i, j in zip(range(self.n_elements), range(1, self.n_elements)):
                unswapped = self.pairwise_graph_weight(i, j)
                self[i], self[j] = self[j], self[i]

                swapped = self.pairwise_graph_weight(i, j)

                if swapped > unswapped:
                    self[i], self[j] = self[j], self[i]
                else:
                    swapped |= True

            # If no elements were swapped then break
            if not swapped:
                break

    def pairwise_graph_weight(self, i, j):
        '''
            Calculates the intersections between two elements of the map
        '''
        if self[i] > self[j]:
            i, j = j, i

        pairwise_weight = 0
        for edges_i in self.graph[i]:
            for edges_j in self.graph[j]:
                if self.position_x_group(edges_i) > self.position_x_group(edges_j):
                    pairwise_weight += 1
        return pairwise_weight

    def graph_weight(self):
        '''
            Calculates the weight of all intersections on the map
        '''
        weight = 0
        for i in range(self.n_elements):  # Ordered by current map
            stab_lower = self.graph[i]
            for stab_upper in self.graph[i + 1:]:
                for edge_lower in stab_lower:
                    for edge_upper in stab_upper:
                        if self.position_x_group(edge_lower) > self.position_x_group(edge_upper):
                            weight += 1
        return weight

class LinearWeightSortMapper(BaseWeightSortMapper):
    '''
        Dispatch class for namespace clarity
    '''
    pass

class CombWeightSortMapper(comb_mapper.BaseCombMapper, BaseWeightSortMapper):
    '''
        Dispatch class for namespace clarity
    '''
    def mapping_fn(self, *args, **kwargs): 
        BaseWeightSortMapper.mapping_fn(self, *args, **kwargs) 
