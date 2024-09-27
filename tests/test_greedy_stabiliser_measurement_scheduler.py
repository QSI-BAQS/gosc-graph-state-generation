import unittest
from graph_state_generation.graph_state import graph_state, graph_node 
from graph_state_generation.graph_state import graph_state, graph_node, example_graphs
from graph_state_generation.mappers import linear_mapper
from graph_state_generation.schedulers.greedy_stabiliser_measurement_scheduler import GreedyStabiliserMeasurementSchedulerLeft


class WeightedMapperTest(unittest.TestCase):

    def test_small_instance(self): 
        graph = graph_state.GraphState(3) 

        graph[0].append(*[1, 2])
        graph[1].append(*[0])
        graph[2].append(*[0])

        mapper = linear_mapper.LinearMapper(graph)
        sched = GreedyStabiliserMeasurementSchedulerLeft(graph, mapper) 
        # No state prep reductions applied here and all 
        # stabilisers share a dependency on qubits 0
        assert(len(sched) == 3)

    def test_tree_instances(self, n_qubits=10): 
        graph = example_graphs.graph_binary_tree(n_qubits) 
        mapper = linear_mapper.LinearMapper(graph)
        sched = GreedyStabiliserMeasurementSchedulerLeft(graph, mapper) 
        assert(len(sched) < len(graph))


if __name__ == '__main__':
    unittest.main()
