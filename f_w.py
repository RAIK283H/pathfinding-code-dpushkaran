import math
from graph_data import graph_data
from pathing import getDistance

def refactor_adj_to_matrix(graph):

    length = len(graph)
    mx = []

    for i in range(length):
        row = [math.inf] * length
        mx.append(row) 

    for i in range(length):
        mx[i][i] = 0
        for neighbor in graph[i][1]:
            mx[i][neighbor] = getDistance(graph[i][0], graph[neighbor][0])

    return mx

def f_w(graph):

    distance_matrix = refactor_adj_to_matrix(graph)
    length = len(graph)
    parent_matrix = []

    for src_node in range(length):
        r = [None] * length 
        parent_matrix.append(r)

    for src_node in range(length):
        for neighbor in graph[src_node][1]:
            parent_matrix[src_node][neighbor] = src_node

    for i_node in range(length):
        for src_node in range(length):
            for dest_node in range(length):
                if distance_matrix[src_node][dest_node] > distance_matrix[src_node][i_node] + distance_matrix[i_node][dest_node]:
                    distance_matrix[src_node][dest_node] = distance_matrix[src_node][i_node] + distance_matrix[i_node][dest_node]
                    parent_matrix[src_node][dest_node] = parent_matrix[i_node][dest_node]

    return distance_matrix, parent_matrix

def reconstruct_path(parent, start, end): 
    path = []

    while end is not None:
        path.append(end)
        end = parent[start][end]

    path.reverse()

    return path

def run_floyd_warshall_and_print_paths(graph_data):
    for graph_index, graph in enumerate(graph_data):

        true_index = (graph_index +1)
        print("Graph #" + str(true_index))

        distances, parents = f_w(graph)
        
        start_node = 0
        end_node = len(graph) - 1

        path = reconstruct_path(parents, start_node, end_node)

        print(f"Shortest path from Node {start_node} to Node {end_node} is: {path}")
        print(f"Distance: {distances[start_node][end_node]}")

        print("--------------------------------------------------------------")

run_floyd_warshall_and_print_paths(graph_data)
