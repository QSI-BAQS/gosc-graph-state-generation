import unittest
from graph_state_generation.graph_state import graph_state, graph_node
from graph_state_generation.mappers import weight_sort_mapper

class WeightedMapperTest(unittest.TestCase):

    def test_small_instance(self):
        small_graph = graph_state.GraphState(3)

        small_graph[0].append(*[1, 2])
        small_graph[1].append(*[0])
        small_graph[2].append(*[0])

        mapper = weight_sort_mapper.LinearWeightSortMapper(small_graph)


if __name__ == '__main__':
    unittest.main()
