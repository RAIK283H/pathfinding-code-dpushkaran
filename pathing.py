import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    currentGraphIndex = global_game_data.current_graph_index
    assert 0 <= currentGraphIndex < len(graph_data.graph_data), "The current graph index does not exist."

    startNodeIndex = 0
    endNodeIndex = len(graph_data.graph_data[currentGraphIndex])-1
    targetNodeIndex = global_game_data.target_node[currentGraphIndex]

    assert 0 <= targetNodeIndex < len(graph_data.graph_data[currentGraphIndex]), "Target node doesn't exist in the current graph."
    assert startNodeIndex is not None, "Start node is not empty"
    assert endNodeIndex is not None, "End node is empty"

    currentNodeIndex = startNodeIndex
    path = [currentNodeIndex]
    
    #Loops until the target node is hit and randomly selects a node within the adjacet list
    while(currentNodeIndex != targetNodeIndex):
        adjacentList = graph_data.graph_data[currentGraphIndex][currentNodeIndex][1]
        currentNodeIndex = int(random.choice(adjacentList))
        path.append(currentNodeIndex)

    # Checks if the target node is actually hit 
    assert currentNodeIndex == targetNodeIndex, "Did not hit the target node."

    #Loops until the end node is hit and randomly selects a node within the adjacet list
    while(currentNodeIndex != endNodeIndex):
        adjacentList = graph_data.graph_data[currentGraphIndex][currentNodeIndex][1]
        currentNodeIndex = int(random.choice(adjacentList))
        path.append(currentNodeIndex)

    #Post Condition the path ends on the end node
    assert currentNodeIndex == endNodeIndex, "Did not end at the end node."
    #Post Condition the path has nodes in its list
    assert len(path) > 0, "The path does not have any nodes to hit."

    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
