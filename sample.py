import heapq

graph = {
    'S': {'neighbors': {'A': 3, 'B': 1}, 'heuristic': 7},
    'A': {'neighbors': {'B': 2, 'C': 2}, 'heuristic': 5},
    'B': {'neighbors': {'C': 3}, 'heuristic': 7},
    'C': {'neighbors': {'D': 4, 'G': 4}, 'heuristic': 4},
    'D': {'neighbors': {'G': 1}, 'heuristic': 1},
    'G': {'neighbors': {}, 'heuristic': 0}
}

def depth_first_search_tree(graph, start, goal):
    stack = [(start, [])]
    expanded_nodes = []
    while stack:
        node, path = stack.pop()
        expanded_nodes.append(node)
        if node == goal:
            return (
                "Depth-First Search (Tree Search):",
                path + [node],
                expanded_nodes,
                list(set(graph.keys()) - set(expanded_nodes))
            )
        neighbors = list(graph[node]['neighbors'])
        unexpanded_neighbors = list(set(neighbors) - set(expanded_nodes))
        stack.extend((neighbor, path + [node]) for neighbor in reversed(unexpanded_neighbors))

result = depth_first_search_tree(graph, 'S', 'G')
print("Path:", result[1])
print("Expanded Nodes:", result[2])
print("Nodes Not Expanded:", result[3])
