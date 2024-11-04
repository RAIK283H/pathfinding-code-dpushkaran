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
    
    

