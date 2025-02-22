import numpy as np
import heapq
import matplotlib.pyplot as plt

# Directions (4-way movement)
DIRECTIONS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Directions (8-way movement)
DIRECTIONS_8 = [(0, 1), (1, 1), (1, 0), (1, -1),
                (0, -1), (-1, -1), (-1, 0), (-1, 1)]


class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g  # Cost to reach this node
        self.h = h  # Heuristic cost
        self.f = g + h  # Total cost

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b, diagonal=False):
    """ Compute heuristic distance between points a and b. """
    if diagonal:
        return np.linalg.norm(np.array(a) - np.array(b))  # Euclidean distance
    else:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance


def astar(grid, start, goal, diagonal=False):
    """A* algorithm"""
    open_list = []
    closed_set = set()
    directions = DIRECTIONS_8 if diagonal else DIRECTIONS_4

    start_node = Node(start, None, 0, heuristic(start, goal, diagonal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.position)

        for d in directions:
            neighbor_pos = (current_node.position[0] + d[0], current_node.position[1] + d[1])

            if (0 <= neighbor_pos[0] < grid.shape[0] and
                    0 <= neighbor_pos[1] < grid.shape[1] and
                    grid[neighbor_pos] == 0 and
                    neighbor_pos not in closed_set):
                g = current_node.g + (1.414 if diagonal and abs(d[0]) + abs(d[1]) == 2 else 1)
                h = heuristic(neighbor_pos, goal, diagonal)
                neighbor_node = Node(neighbor_pos, current_node, g, h)

                heapq.heappush(open_list, neighbor_node)

    return None  # No path found


def bfs(grid, start, goal):
    """Breadth-First Search"""
    from collections import deque
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (current, path) = queue.popleft()
        if current == goal:
            return path + [current]

        if current in visited:
            continue

        visited.add(current)

        for d in DIRECTIONS_4:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if (0 <= neighbor[0] < grid.shape[0] and
                    0 <= neighbor[1] < grid.shape[1] and
                    grid[neighbor] == 0 and
                    neighbor not in visited):
                queue.append((neighbor, path + [current]))

    return None  # No path found


def ucs(grid, start, goal):
    """Uniform Cost Search"""
    open_list = [(0, start, [])]  # (cost, position, path)
    visited = set()

    while open_list:
        cost, current, path = heapq.heappop(open_list)

        if current == goal:
            return path + [current]

        if current in visited:
            continue

        visited.add(current)

        for d in DIRECTIONS_4:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if (0 <= neighbor[0] < grid.shape[0] and
                    0 <= neighbor[1] < grid.shape[1] and
                    grid[neighbor] == 0 and
                    neighbor not in visited):
                heapq.heappush(open_list, (cost + 1, neighbor, path + [current]))

    return None  # No path found


def plot_path(grid, path, title):
    """Plot the grid and path"""
    plt.imshow(grid, cmap='gray_r')
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, marker="o", color="red")
    plt.title(title)
    plt.show()


# Example Grid (0 = free space, 1 = obstacle)
grid = np.array([
    [0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]])

start = (0, 0)
goal = (4, 6)

# Run Algorithms
path_astar = astar(grid, start, goal)
path_bfs = bfs(grid, start, goal)
path_ucs = ucs(grid, start, goal)

# Plot Results
plot_path(grid, path_astar, "A* Path")
plot_path(grid, path_bfs, "BFS Path")
plot_path(grid, path_ucs, "UCS Path")