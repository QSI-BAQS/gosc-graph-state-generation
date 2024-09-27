import unittest
from graph_state_generation.graph_state import example_graphs 

class WeightedMapperTest(unittest.TestCase):

    def test_no_adjacencies(self, n_qubits=10): 
        graph = example_graphs.graph_no_adjacencies(n_qubits)
        assert(len(graph) == n_qubits)

        for vert in graph:
            assert(len(vert) == 0) 

    def test_no_adjacencies_range(self): 
        for i in range(100, 1000, 47):
            self.test_no_adjacencies(n_qubits=i)


    def test_disconnected_bipartied(self, n_qubits=11): 
        graph = example_graphs.graph_disconnected_bipartied(n_qubits)
        assert(len(graph) == n_qubits)
        for vert in graph:
            if n_qubits % 2 == 0:
                assert(len(vert) == 1) 
            else:
                if vert.qubit_idx < n_qubits - 1: 
                    assert(len(vert) == 1) 
                else:
                    assert(len(vert) == 0) 

    def test_disconnected_bipartied_range(self): 
        for i in range(100, 1000, 47):
            self.test_disconnected_bipartied(n_qubits=i)


if __name__ == '__main__':
    unittest.main()
