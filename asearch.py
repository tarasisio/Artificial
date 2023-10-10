import heapq

def astar_search(graph, start, goal, heuristic):
    open_set = [(0, start)]  # Priority queue: (f(n), node)
    g_values = {node: float('infinity') for node in graph}
    g_values[start] = 0
    came_from = {}  # Initialize the dictionary to store parent nodes
    
    while open_set:
        f, current_node = heapq.heappop(open_set)
        
        if current_node == goal:
            # Path found, reconstruct and return it
            path = []
            while current_node != start:
                path.insert(0, current_node)  # Insert node at the beginning of the path
                current_node = came_from[current_node]
            path.insert(0, start)
            return path
        
        for neighbor, weight in graph.get(current_node, {}).items():
            tentative_g = g_values[current_node] + weight
            if tentative_g < g_values.get(neighbor, float('infinity')):
                # This path to the neighbor is better than any previous one
                g_values[neighbor] = tentative_g
                f = tentative_g + heuristic.get(neighbor, 0)  # Use 0 as default heuristic value if not provided
                heapq.heappush(open_set, (f, neighbor))
                came_from[neighbor] = current_node
    
    return None  # No path found

# Example usage
weighted_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'B': {'C': 3, 'S': 1, 'A': 2},
    'C': {'A': 2, 'D': 4, 'B': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'D': 1, 'C': 4}
}

heuristic_values = {
    'S': 7,
    'B': 7,
    'A': 5,
    'C': 4,
    'D': 1,
    'G': 0
}

# Start and goal nodes
start_node = 'S'
goal_node = 'G'

# Run A* search
path = astar_search(weighted_graph, start_node, goal_node, heuristic_values)

if path:
    print("A* Search Path from 'S' to 'G':", ' -> '.join(path))
else:
    print("No valid path found from 'S' to 'G' using A* Search.")
