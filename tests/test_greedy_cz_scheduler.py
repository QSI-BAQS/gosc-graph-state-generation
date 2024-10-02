import unittest
from graph_state_generation.graph_state import graph_state, graph_node, example_graphs
from graph_state_generation.mappers import linear_mapper
from graph_state_generation.schedulers import greedy_cz_scheduler 


class WeightedMapperTest(unittest.TestCase):

    def test_small_instance(self): 
        graph = graph_state.GraphState(3) 

        graph[0].append(*[1, 2])
        graph[1].append(*[0])
        graph[2].append(*[0])

        mapper = linear_mapper.LinearMapper(graph)
        
        sched = greedy_cz_scheduler.GreedyCZScheduler(graph, mapper) 
        assert(len(sched) == 1)

    def test_tree_instances(self, n_qubits=10): 
        graph = example_graphs.graph_binary_tree(n_qubits) 
        mapper = linear_mapper.LinearMapper(graph)
        sched = greedy_cz_scheduler.GreedyCZScheduler(graph, mapper) 
        assert(len(sched) < len(graph))

    def test_range_of_instances(self):
        for n_qubits in range(100, 1000, 47):
            self.test_tree_instances(n_qubits)


if __name__ == '__main__':
    unittest.main()
