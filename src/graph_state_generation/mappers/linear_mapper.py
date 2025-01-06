'''
    Linear Mapper
'''
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
            self[i] = i

    def position_xy(self, qubit_index: int) -> tuple[int, int]:
        '''
            Returns qubit position given qubit_idx
        '''
        return (self[qubit_index], 0)

    def position_x_group(self, qubit_index: int) -> int:
        return self[qubit_index]

    def position_y_group(self, qubit_index: int) -> int:
        return 0 
