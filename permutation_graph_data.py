
graph_data = [

    [
        [(0, 0), [1]],           # Node 0 connected to Node 1
        [(0, 100), [0, 2]],      # Node 1 connected to Nodes 0 and 2
        [(0, 200), [1]],         # Node 2 connected to Node 1 (end node)
    ],

    # Graph 2: Small cycle (4 nodes)
    [
        [(0, 0), [1]],           # Node 0 connected to Node 1
        [(100, 0), [0, 2]],      # Node 1 connected to Nodes 0 and 2
        [(100, 100), [1, 3]],    # Node 2 connected to Nodes 1 and 3
        [(0, 100), [2]],         # Node 3 connected to Node 2 (end node)
    ],

    # Graph 3: Slightly larger cycle with branching paths (5 nodes)
    [
        [(0, 0), [1]],           # Node 0 connected to Node 1
        [(100, 0), [0, 2, 3]],   # Node 1 connected to Nodes 0, 2, and 3
        [(200, 0), [1]],         # Node 2 connected to Node 1
        [(100, 100), [1, 4]],    # Node 3 connected to Nodes 1 and 4
        [(200, 100), [3]],       # Node 4 connected to Node 3 (end node)
    ],

    # Graph 4: Longer path with more nodes (6 nodes)
    [
        [(0, 0), [1]],           # Node 0 connected to Node 1
        [(100, 0), [0, 2]],      # Node 1 connected to Nodes 0 and 2
        [(200, 0), [1, 3]],      # Node 2 connected to Nodes 1 and 3
        [(300, 0), [2, 4]],      # Node 3 connected to Nodes 2 and 4
        [(400, 0), [3, 5]],      # Node 4 connected to Nodes 3 and 5
        [(500, 0), [4]],         # Node 5 connected to Node 4 (end node)
    ],

    # Graph 5: 7 nodes with multiple branching paths
    [
        [(0, 0), [1, 2]],        # Node 0 connected to Nodes 1 and 2
        [(100, 0), [0, 3]],      # Node 1 connected to Nodes 0 and 3
        [(0, 100), [0, 3]],      # Node 2 connected to Nodes 0 and 3
        [(100, 100), [1, 2, 4]], # Node 3 connected to Nodes 1, 2, and 4
        [(200, 100), [3, 5, 6]], # Node 4 connected to Nodes 3, 5, and 6
        [(300, 100), [4]],       # Node 5 connected to Node 4
        [(200, 200), [4]],       # Node 6 connected to Node 4 (end node)
    ],

    # Graph 6: Small graph with more complex paths (8 nodes)
    [
        [(0, 0), [1, 2]],        # Node 0 connected to Nodes 1 and 2
        [(100, 0), [0, 3]],      # Node 1 connected to Nodes 0 and 3
        [(0, 100), [0, 3]],      # Node 2 connected to Nodes 0 and 3
        [(100, 100), [1, 2, 4]], # Node 3 connected to Nodes 1, 2, and 4
        [(200, 100), [3, 5, 6]], # Node 4 connected to Nodes 3, 5, and 6
        [(300, 100), [4]],       # Node 5 connected to Node 4
        [(200, 200), [4, 7]],    # Node 6 connected to Nodes 4 and 7
        [(300, 200), [6]],       # Node 7 connected to Node 6 (end node)
    ],

    # Graph 7: Slightly larger with a closed loop (9 nodes)
    [
        [(0, 0), [1]],           # Node 0 connected to Node 1
        [(0, 100), [0, 2, 3]],   # Node 1 connected to Nodes 0, 2, and 3
        [(100, 100), [1, 4]],    # Node 2 connected to Nodes 1 and 4
        [(0, 200), [1, 5]],      # Node 3 connected to Nodes 1 and 5
        [(200, 100), [2, 6]],    # Node 4 connected to Nodes 2 and 6
        [(100, 200), [3, 6]],    # Node 5 connected to Nodes 3 and 6
        [(150, 150), [4, 5, 7]], # Node 6 connected to Nodes 4, 5, and 7
        [(200, 200), [6, 8]],    # Node 7 connected to Nodes 6 and 8
        [(300, 200), [7]],       # Node 8 connected to Node 7 (end node)
    ],
    
]
