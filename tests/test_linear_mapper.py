import unittest
from graph_state_generation.mappers import linear_mapper 

class DummyGraph: 
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices

class LinearMapperTest(unittest.TestCase):

    def test_small_instance(self, n_elements=10): 
        graph = DummyGraph(n_elements) 
        mapper = linear_mapper.LinearMapper(graph)
        for i in range(n_elements):
            assert(mapper[i] == i)


    def test_range_of_instances(self):        
        for i in range(10, 1000, 100):
            self.test_small_instance(n_elements=i)

if __name__ == '__main__':
    unittest.main()
