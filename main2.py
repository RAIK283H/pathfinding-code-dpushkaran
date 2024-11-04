from permutation_graph_data import graph_data
from permutation import find_hamilton_cycle

def main():
    results = []
    graphIndex = 1
    
    for graph in graph_data:
        result = find_hamilton_cycle(graph)
        results.append(result)

        print("Graph " + str(graphIndex) + ":")
        if result == -1:
            print("No Hamiltonian cycle exists.\n")
        else:
            for cycle in result:
                print(" -> ".join(map(str, cycle)))

            print("\n")
        graphIndex += 1
    
    return results

if __name__ == "__main__":
    main()