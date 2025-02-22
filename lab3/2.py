import heapq


def heuristic(cell, treasure):
    return abs(cell[0] - treasure[0]) + abs(cell[1] - treasure[1])


def get_neighbors(cell, grid):
    neighbors = []
    x, y = cell
    rows, cols = len(grid), len(grid[0])
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1:
            neighbors.append((nx, ny))
    return neighbors


def best_first_search(grid, start, treasure):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start, treasure), start))
    visited = set()
    parent = {start: None}

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current == treasure:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        visited.add(current)

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic(neighbor, treasure), neighbor))
                parent[neighbor] = current

    return None


grid = [
    [0, 0, 0, 0],
    [0, -1, 0, -1],
    [0, 0, 0, 0],
    [0, -1, 0, 0]
]
start = (0, 0)
treasure = (3, 3)

path = best_first_search(grid, start, treasure)
print("Path to Treasure:", path)
