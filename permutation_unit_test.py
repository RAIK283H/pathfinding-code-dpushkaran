import unittest
from permutation import sjt_Permutations, find_hamilton_cycle

class TestSJTandHamiltonianCycle(unittest.TestCase):

    #Test SJT algorithm for a small set of permutations (n = 3)
    def test_sjt_permutations_small(self):
        expected = [
            [1, 2],
            [2, 1]
        ]
        result = list(sjt_Permutations(3))
        self.assertEqual(result, expected, "SJT permutations for n=3 did not match expected output.")

    # Test SJT algorithm for a medium set of permutations (n = 4)
    def test_sjt_permutations_medium(self):
        expected = [
            [1, 2, 3],
            [2, 1, 3],
            [2, 3, 1],
            [3, 2, 1],
            [3, 1, 2],
            [1, 3, 2]
        ]
        result = list(sjt_Permutations(4))
        self.assertEqual(result, expected, "SJT permutations for n=4 did not match expected output.")

    #Test for a graph with a known Hamiltonian cycle
    def test_hamiltonian_cycle_exists(self):
        graph = [
            [(0, 0), [1, 2]],
            [(1, 0), [0, 2, 3]],
            [(0, 1), [0, 1, 3]],
            [(1, 1), [1, 2]]
        ]
        result = find_hamilton_cycle(graph)
        expected = [[1, 2, 3, 0]]  # Example cycle (actual result depends on implementation specifics)
        self.assertIn(expected[0], result, "Hamiltonian cycle detection failed on known cycle graph.")

    def test_multiple_hamiltonian_cycles(self):
        # Define a graph with multiple Hamiltonian cycles (like the revised Graph 8)
        graph = [
            [(0, 0), [1, 2]],        # Node 0 (start node) connected to Nodes 1 and 2
            [(100, 0), [0, 2, 3, 4]],   # Node 1 connected to Nodes 0, 2, 3, and 4
            [(0, 100), [0, 1, 3, 4]],   # Node 2 connected to Nodes 0, 1, 3, and 4
            [(100, 100), [1, 2, 4, 5]], # Node 3 connected to Nodes 1, 2, 4, and 5
            [(50, 150), [1, 2, 3, 5]],  # Node 4 connected to Nodes 1, 2, 3, and 5
            [(150, 150), [3, 4]]        # Node 5 (end node) connected to Nodes 3 and 4
        ]
        
        # Run the find_hamilton_cycle function
        result = find_hamilton_cycle(graph)

        # Expected Hamiltonian cycles (some possible paths for illustration)
        expected_cycles = [
            [0, 1, 2, 3, 4, 5],
            [0, 1, 3, 2, 4, 5],
            [0, 1, 4, 2, 3, 5],
            [0, 2, 1, 3, 4, 5],
            [0, 2, 3, 1, 4, 5],
            [0, 2, 4, 1, 3, 5]
            # Other possible cycles may be added here
        ]

        # Verify that we have multiple Hamiltonian cycles
        self.assertIsInstance(result, list, "Expected a list of Hamiltonian cycles.")
        self.assertGreaterEqual(len(result), len(expected_cycles), "Expected multiple Hamiltonian cycles.")

        # Check that each expected cycle is in the result
        for cycle in expected_cycles:
            self.assertIn(cycle, result, f"Expected cycle {cycle} not found in result.")

    
    #Test for a graph that does not have a Hamiltonian cycle
    def test_no_hamiltonian_cycle(self):
        graph = [
            [(0, 0), [1]],
            [(1, 0), [0, 2]],
            [(2, 0), [1, 3]],
            [(3, 0), [2]]
        ]
        result = find_hamilton_cycle(graph)
        self.assertEqual(result, -1, "Hamiltonian cycle detection incorrectly found a cycle where none exists.")
    
    

