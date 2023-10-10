from collections import deque

def breadth_first_search(graph, start, goal):
    queue = deque([(start, [start])])  # Queue of (node, path) tuples
    visited = set()

    while queue:
        current_node, path = queue.popleft()

        if current_node == goal:
            return path  # Path found

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # No valid path found

# Given graph
weighted_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'B': {'C': 3, 'S': 1, 'A': 2},
    'C': {'A': 2, 'D': 4, 'B': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'D': 1, 'C': 4}
}

# Start and goal nodes
start_node = 'S'
goal_node = 'G'

# Find the breadth-first search path
bfs_path = breadth_first_search(weighted_graph, start_node, goal_node)

if bfs_path:
    print("Breadth-First Search Path from 'S' to 'G':", ' -> '.join(bfs_path))
else:
    print("No valid path found from 'S' to 'G' using Breadth-First Search.")
