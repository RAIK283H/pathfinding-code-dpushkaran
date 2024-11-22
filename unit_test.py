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
    
    #Checks dfs
    def test_dfs_path(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = [1]  # Set the target node to node 1 for testing
        
        startIndex = 0
        targetIndex = global_game_data.target_node[global_game_data.current_graph_index]
        endIndex = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
        
        path = pathing.get_dfs_path()

       #Preconditions
        self.assertEqual(path[0], startIndex, "DFS: Doesn't start at start node")
        self.assertEqual(path[-1], endIndex, "DFS: Doesn't end at end node")

        # Postcondition
        self.assertIn(targetIndex, path, "DFS: The path doesn't contain the target.")
        
        # Valid path
        graph = graph_data.graph_data[global_game_data.current_graph_index]
        for i in range(len(path) - 1):
            self.assertIn(path[i+1], graph[path[i]][1], "DFS: Two nodes are not connected")

    # Test BFS path
    def test_bfs_path(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = [1]  

        startIndex = 0
        targetIndex = global_game_data.target_node[global_game_data.current_graph_index]
        endIndex = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
        
        path = pathing.get_bfs_path()

        # Preconditions
        self.assertEqual(path[0], startIndex, "BFS:Doesn't start at start node")
        self.assertEqual(path[-1], endIndex, "BFS: Doesn't end at end node.")

        # Postcondition
        self.assertIn(targetIndex, path, "BFS: The path doesn't contain the target.")
        
        # Valid Graph
        graph = graph_data.graph_data[global_game_data.current_graph_index]
        for i in range(len(path) - 1):
            self.assertIn(path[i+1], graph[path[i]][1], "Two nodes are not conencted")
    

    def test_dijkstra_path_start_and_end(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = [1]  # Example target node

        path = pathing.get_dijkstra_path()

        startNodeIndex = 0
        endNodeIndex = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

        
        self.assertEqual(path[0], startNodeIndex, "Dijkstra: Path does not start at the correct node.")
        self.assertEqual(path[-1], endNodeIndex, "Dijkstra: Path does not end at the correct node.")

    def test_dijkstra_path_contains_target(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = [2]

        path = pathing.get_dijkstra_path()
        targetNode = global_game_data.target_node[global_game_data.current_graph_index]

        self.assertIn(targetNode, path, "Dijkstra: Path does not include the target node.")

    
if __name__ == '__main__':
    unittest.main()
