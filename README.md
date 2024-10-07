# Pathfinding Starter Code
Customer Requirements:
1. The node you start at should be classified as the start node which is the first node in each index of graph data element
2. A target node should be defined
3. A end node should be defined as the last node at each index of graph data element
4. Then a graph path should be generated randomly for the random player.
5. The graph path should start at start end at end and at some point hit the target node

Random Path Generation:
My random path generation works by accessing the adjacent list for the current node. From there it will randomly select an element from that list and update that as the next node to go to. While that node is not the target node those actions will continue to happen. Once the target node has been hit those same actions will occure except until the end node has been hit. Everytime a node is hit it is added to the path and then that is returned.

Statistic added:
The statistic I added was how many nodes were hit with each path. Rather than just taking the length of the path list I decided to add a count for when a node was hit because sometimes when a path hits the same node twice that wouldn't be counted. I also chose this method so that the user could see the element being updated in real time and allow them to compare to the pathes before it.
