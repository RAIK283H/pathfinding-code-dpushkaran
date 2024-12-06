import unittest
import f_w
import math
from graph_data import graph_data
from pathing import getDistance

test_graph_1 = [
    [(0, 0), [1]],
    [(100, 0), [0, 2]],
    [(200, 0), [1]],
]

test_graph_2 = [
    [(0, 0), [1, 2]],
    [(100, 0), [0, 2]],
    [(50, 50), [0, 1]],
]

class TestFloydWarshall(unittest.TestCase):
    def test_adjacency_list_to_matrix(self):
    
        expected_matrix_1 = [
            [0, 100, math.inf],
            [100, 0, 100],
            [math.inf, 100, 0],
        ]
        result_matrix_1 = f_w.refactor_adj_to_matrix(test_graph_1)
        self.assertEqual(result_matrix_1, expected_matrix_1)

        expected_matrix_2 = [
            [0, 100, 70.71],
            [100, 0, 70.71],
            [70.71, 70.71, 0],
        ]
        result_matrix_2 = f_w.refactor_adj_to_matrix(test_graph_2)
        for i in range(len(result_matrix_2)):
            for j in range(len(result_matrix_2[i])):
                self.assertAlmostEqual(result_matrix_2[i][j], expected_matrix_2[i][j], places=2)

    def test_floyd_warshall(self):
        
        distances, parents = f_w.f_w(test_graph_1)
        expected_distances_1 = [
            [0, 100, 200],
            [100, 0, 100],
            [200, 100, 0],
        ]
        for i in range(len(distances)):
            for j in range(len(distances[i])):
                self.assertAlmostEqual(distances[i][j], expected_distances_1[i][j], places=2)

        
        distances, parents = f_w.f_w(test_graph_2)
        expected_distances_2 = [
            [0, 100, 70.71],
            [100, 0, 70.71],
            [70.71, 70.71, 0],
        ]
        for i in range(len(distances)):
            for j in range(len(distances[i])):
                self.assertAlmostEqual(distances[i][j], expected_distances_2[i][j], places=2)

    def test_reconstruct_path(self):
        
        _, parents = f_w.f_w(test_graph_1)
        path = f_w.reconstruct_path(parents, 0, 2)
        self.assertEqual(path, [0, 1, 2])

        _, parents = f_w.f_w(test_graph_2)
        path = f_w.reconstruct_path(parents, 0, 1)
        self.assertEqual(path, [0, 1])

if __name__ == "__main__":
    unittest.main()
