def sjt_Permutations(length):

    # list of nodes
    permutations = list(range(1,length))
    #list of directions for each node
    directions = [-1] * (length-1)
    #initial permuation as a list
    perm = [permutations[:]]

    while True:
        largest_mobile_number = -1
        largest_mobile_index = -1

        for i in range(len(permutations)):
            adjacent_index = i + directions[i]
            if 0 <= adjacent_index < len(permutations) and permutations[i] > permutations[adjacent_index]:
                if permutations[i] > largest_mobile_number:
                    largest_mobile_number = permutations[i]
                    largest_mobile_index = i
        
        if largest_mobile_index < 0:
            return perm
        
        adjacent_index = directions[largest_mobile_index] + largest_mobile_index

        temp = permutations[largest_mobile_index]
        permutations[largest_mobile_index] = permutations[adjacent_index]
        permutations[adjacent_index] = temp

        temp = directions[largest_mobile_index]
        directions[largest_mobile_index] = directions[adjacent_index]
        directions[adjacent_index] = temp

        for i in range(len(permutations)):
            if permutations[i] > largest_mobile_number:
                directions[i] *= -1

        perm.append(permutations[:])

    return perm

def is_cycle(permutation, graph, start, end):
    current = start
    for node in permutation:
        if node not in graph[current][1]:
            return False
        current = node
    return end in graph[current][1]

def find_hamilton_cycle(graph):
    length = len(graph)
    start = 1
    end = length -1
    cycles = []

    for permutation in sjt_Permutations(length -2):
        temp = []
        for perm in permutation:
            temp.append(perm + 1)
        permutation = temp

        if is_cycle(permutation, graph, start, end):
            cycles.append([start] + permutation + [end])
    
    if(len(cycles) > 0):
        return cycles
    return -1
    