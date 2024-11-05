from permutation_graph_data import graph_data
from permutation import find_hamilton_cycle, optimal_hamilton_cycle, sjt_Permutations

def main():
    results = []
    graphIndex = 1
    
    for graph in graph_data:

        length = len(graph)
        result = find_hamilton_cycle(graph)
        results.append(result)

        print("Graph " + str(graphIndex) + ":")
        if result == -1:
            print("No Hamiltonian cycle exists.\n")
        else:
            print("All Hamiltonian cycles:")
            for cycle in result:
                print(" -> ".join(map(str, cycle)))

            optimal_cycles, min_distance = optimal_hamilton_cycle(graph, result)
            print("\nOptimal Hamiltonian cycle(s) with minimum distance:", min_distance)
            for optimal_cycle in optimal_cycles:
                print(" -> ".join(map(str, optimal_cycle)))

            print("\n")
        graphIndex += 1
    
    return results

if __name__ == "__main__":
    main()