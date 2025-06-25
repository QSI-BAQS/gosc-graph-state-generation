'''
    Comb Mapper
'''
from graph_state_generation.mappers import mapper


class BaseCombMapper(mapper.Mapper):
    '''
        Comb Mapper
        Maps qubit i to position i
    '''
    def __init__(
        self,
        graph,  # Graph obj
        height: int,  # Height of comb region
        width: int,  # Width of comb region
        *args, 
        comb_spacing: int = 1,  # Spacing
        **kwargs
    ):
        '''
Constructor for a comb mapper
    :: graph : Graph :: Graph object
    :: height : int :: Height of region
    :: width : int :: Width of region
    :: comb_spacing : int :: Spacing between 
tines
    :: comb_width : int :: Width of tine 
        '''
        self.height = height
        self.width = width
        self.comb_spacing = comb_spacing

        # TODO: UNDERFULL
        self.tine_width = 2 + self.comb_spacing

        self.n_tines = (width // (self.tine_width))  
        self.tine_size = height * 2

        if self.n_tines * self.height * 2 < len(graph): 
            raise IndexError("Not enough registers", graph)

        super().__init__(graph, *args, **kwargs)

    def _tine(self, index): 
        '''
            Given index returns tine
        '''
        return index // self.tine_size 

    def _offset(self, index):
        '''
            Given index, returns offset from top 
        '''
        return index % self.height

    def _lr(self, index):
        return (index // self.height) % 2 

    def mapping_fn(self, *args, **kwargs):
        '''
        mapper_fn
        Linear map
        '''
        for i in range(self.n_elements):
            self[i] = i

    def position_xy(self, qubit_index):
        mapped_index = self[qubit_index] 

        tine_idx = self._tine(mapped_index) 
        lr_idx = self._lr(mapped_index)
        x_pos = tine_idx * self.tine_width + (lr_idx * (self.tine_width - 1)) 
        y_pos = self._offset(mapped_index)
        return (x_pos, y_pos)

    def iter_xy(self):
        for i in range(self.n_elements):
            yield self.position_xy(i)

    def iter_tine(self):
        for i in range(self.n_elements):
            mapped_index = self[i] 
            yield self._tine(mapped_index)

    def position_x_group(self, qubit_index: int) -> int:
        return self._tine(qubit_index)

    def position_y_group(self, qubit_index: int) -> int:
        return self._offset(qubit_index) 

class CombMapper(BaseCombMapper):
    '''
        Dispatch class for namespace clarity
    '''
    pass
