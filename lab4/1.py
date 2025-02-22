import heapq
from collections import deque

def uniform_cost_search(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, []))
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]

        if node == goal:
            return path, cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))
    return None, float('inf')

def bfs_unweighted(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

graph_weighted = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('E', 1)],
    'D': [('B', 2), ('E', 1)],
    'E': [('B', 5), ('C', 1), ('D', 1)]
}

graph_unweighted = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['B', 'C', 'D']
}

ucs_path, ucs_cost = uniform_cost_search(graph_weighted, 'A', 'E')
bfs_path = bfs_unweighted(graph_unweighted, 'A', 'E')

print("Uniform Cost Search:", ucs_path, "Cost:", ucs_cost)
print("BFS (Unweighted):", bfs_path)