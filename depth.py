# Given graph
weighted_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'B': {'C': 3, 'S': 1, 'A': 2},
    'C': {'A': 2, 'D': 4, 'B': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'D': 1, 'C': 4}
}

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print("Visiting node:", node)
        visited.add(node)
        for neighbor in graph.get(node, {}):
            dfs(graph, neighbor, visited)

# Perform DFS starting from node 'S'
print("Depth-First Search Results:")
dfs(weighted_graph, 'S')
