'''
    Linear Mapper
'''
from graph_state_generation.mappers import random_mapper

class WeightSortMapper(random_mapper.RandomMapper):
    '''
        Weight sort Mapper
        Attempts to minimise the number of colliding stabilisers via bubble sort 
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
                if self[edges_i] > self[edges_j]:
                    pairwise_weight += 1
        return pairwise_weight


    def graph_weight(self):
        '''
            Calculates the weight of all intersections on the map
        '''
        weight = 0
        for i in range(self.n_elements): # Ordered by current map
            stab_lower = self.graph[i]
            for stab_upper in self.graph[i + 1:]:
                for edge_lower in stab_lower:
                    for edge_upper in stab_upper:
                        if self[edge_lower] > self[edge_upper]:
                            weight += 1
        return weight
