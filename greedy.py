def greedy_search(graph, start, goal, heuristic):
    visited = set()
    path = []
    current_node = start
    
    while current_node != goal:
        if current_node in visited:
            return None  # No path found
        path.append(current_node)
        visited.add(current_node)
        neighbors = graph[current_node]
        if not neighbors:
            return None  # No neighbors, cannot proceed
        current_node = min(neighbors, key=lambda node: neighbors[node] + heuristic[node])  # Greedy choice
        
    path.append(goal)
    return path

# Given graph
weighted_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'B': {'C': 3, 'S': 1, 'A': 2},
    'C': {'A': 2, 'D': 4, 'B': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'D': 1, 'C': 4}
}

# Heuristic values
heuristic_values = {'S': 7, 'B': 7, 'A': 5, 'C': 4, 'D': 1, 'G': 0}

# Perform greedy search from 'S' to 'G'
path = greedy_search(weighted_graph, 'S', 'G', heuristic_values)

if path:
    print("Greedy Search Path from 'S' to 'G':", ' -> '.join(path))
else:
    print("No valid path found from 'S' to 'G' using Greedy Search.")
