import heapq

def dijkstra(graph, start, goal):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            path = []
            while previous_nodes[current_node] is not None:
                path.insert(0, current_node)  # Insert node at the beginning of the path
                current_node = previous_nodes[current_node]
            path.insert(0, start)  # Insert start node at the beginning of the path
            return distances[goal], path

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            total_cost = current_distance + weight
            if total_cost < distances[neighbor]:
                distances[neighbor] = total_cost
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (total_cost, neighbor))

    return float('infinity'), []  # Goal not reachable

# Given graph
weighted_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'B': {'C': 3, 'S': 1, 'A': 2},
    'C': {'A': 2, 'D': 4, 'B': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'D': 1, 'C': 4}
}

# Calculate least uniform cost and path from 'S' to 'G'
least_uniform_cost_to_G, path_to_G = dijkstra(weighted_graph, 'S', 'G')

print("Least Uniform Cost from 'S' to 'G':", least_uniform_cost_to_G)
print("Path from 'S' to 'G':", ' -> '.join(path_to_G))
