from collections import deque

# Given graph
weighted_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'B': {'C': 3, 'S': 1, 'A': 2},
    'C': {'A': 2, 'D': 4, 'B': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'D': 1, 'C': 4}
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print("Visiting node:", node)

        # Enqueue neighbors that are not visited yet
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Perform BFS starting from node 'S'
print("Breadth-First Search Results:")
bfs(weighted_graph, 'S')
