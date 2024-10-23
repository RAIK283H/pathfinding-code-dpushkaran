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

def dfs(graph, start, target):
    stck= [(start, [start])] 
    visitedNodes = set() 
    visitedNodes.add(start)

    while stck:
        currentNode, path = stck.pop()

        # If the current node is the target, return the path
        if currentNode == target:
            return path

        # all nodes
        for adjacentNodes in graph[currentNode][1]:
            if adjacentNodes not in visitedNodes:
                visitedNodes.add(adjacentNodes)
                stck.append((adjacentNodes, path + [adjacentNodes]))

    return []

def bfs(graph, start, target):
    que = [(start, [start])]  
    vistitedNodes = set()  
    vistitedNodes.add(start)

    while que:
        popedNode = que.pop(0)  
        currentNode = popedNode[0]
        path = popedNode[1]

        if currentNode == target:
            return path

        for adjacentNodes in graph[currentNode][1]:
            if adjacentNodes not in vistitedNodes:
                vistitedNodes.add(adjacentNodes)
                que.append((adjacentNodes, path + [adjacentNodes]))

    return [] 




def get_dfs_path():
    currentGraphIndex = global_game_data.current_graph_index
    startNodeIndex = 0  
    targetNodeIndex = global_game_data.target_node[currentGraphIndex]
    endNodeIndex = len(graph_data.graph_data[currentGraphIndex]) - 1  

    # Precoditions
    assert 0 <= startNodeIndex < len(graph_data.graph_data[currentGraphIndex]), "Start node doesn't exist in the current graph."
    assert 0 <= targetNodeIndex < len(graph_data.graph_data[currentGraphIndex]), "Target node doesn't exist in the current graph."
    assert 0 <= endNodeIndex < len(graph_data.graph_data[currentGraphIndex]), "End node doesn't exist in the current graph."

    # Use the standalone dfs function to get paths
    graph = graph_data.graph_data[currentGraphIndex]
    target_path = dfs(graph, startNodeIndex, targetNodeIndex)
    end_path = dfs(graph, targetNodeIndex, endNodeIndex)
    end_path = end_path[1:]

    # Create final path to return
    final_path = target_path + end_path

    # Postconditons
    assert final_path[-1] == endNodeIndex, "The DFS path does not end at the end node."
    assert targetNodeIndex in final_path, "The DFS path does not hit the target node."

    return final_path

def get_bfs_path():
    currentGraphIndex = global_game_data.current_graph_index
    targetNodeIndex = global_game_data.target_node[currentGraphIndex]
    startNodeIndex = 0  
    endNodeIndex = len(graph_data.graph_data[currentGraphIndex]) - 1  

    # Ensure the indices are valid within the graph
    assert startNodeIndex == 0, "The start Node isn't the first node"
    assert 0 <= targetNodeIndex < len(graph_data.graph_data[currentGraphIndex]), "The target node isn't in the current list of possible nodes."
    assert endNodeIndex == len(graph_data.graph_data[currentGraphIndex]) - 1 , "The end Node isn't the last node in the list"

    
    currentGraph = graph_data.graph_data[currentGraphIndex]

    #BFS from start to target
    target_path = bfs(currentGraph, startNodeIndex, targetNodeIndex)
    #BFS from target to end
    end_path = bfs(currentGraph, targetNodeIndex, endNodeIndex)
    end_path = end_path[1:]

    # Combine the two paths for full path
    final_path = target_path + end_path

    # Validate the resulting path
    assert final_path[-1] == endNodeIndex, "The BFS path does not end at the end node."
    assert targetNodeIndex in final_path, "The BFS path does not hit the target node."

    return final_path


def get_dijkstra_path():
    return [1,2]
