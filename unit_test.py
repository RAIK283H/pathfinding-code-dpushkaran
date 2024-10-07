import math
import unittest

# new imports for my tests
import global_game_data
import pathing
import graph_data

class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    #Checks if the start and end node is initalized correctly for the first graph
    def test_path_contains_start_and_end(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = [2] 

        start_node_index = 0
        end_node_index = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
        path = pathing.get_random_path()

        # Check that the first node is the start node and the last node is the end node
        self.assertEqual(path[0], start_node_index, "The path should start at the start node.")
        self.assertEqual(path[-1], end_node_index, "The path should end at the end node.")

if __name__ == '__main__':
    unittest.main()
