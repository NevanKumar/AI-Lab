from collections import deque

# Directions for moving in the maze (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start[0], start[1], [start])])  # Queue of (x, y, path_taken)
    visited[start[0]][start[1]] = True
    nodes_explored = 0

    while queue:
        x, y, path = queue.popleft()
        nodes_explored += 1

        # If we've reached the end, return the path
        if (x, y) == end:
            return path, nodes_explored

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, path + [(nx, ny)]))

    return None, nodes_explored  # No path found


def dfs(maze, start, end, visited, path, nodes_explored):
    x, y = path[-1]
    nodes_explored += 1

    # If we've reached the end, return the path
    if (x, y) == end:
        return path, nodes_explored

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            result, nodes_explored = dfs(maze, start, end, visited, path + [(nx, ny)], nodes_explored)
            if result:
                return result, nodes_explored
            visited[nx][ny] = False  # Backtrack

    return None, nodes_explored  # No path found


def find_path(maze, start, end):
    # BFS for shortest path
    bfs_path, bfs_nodes_explored = bfs(maze, start, end)

    # DFS for any valid path
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visited[start[0]][start[1]] = True
    dfs_path, dfs_nodes_explored = dfs(maze, start, end, visited, [start], 0)

    # Output the results
    print("BFS Path:", bfs_path)
    print("Nodes explored by BFS:", bfs_nodes_explored)
    print("DFS Path:", dfs_path)
    print("Nodes explored by DFS:", dfs_nodes_explored)

    return bfs_path, dfs_path


# Example maze: 0 is wall, 1 is path
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

# Define start and end points
start = (0, 0)
end = (4, 4)

# Find paths using BFS and DFS
find_path(maze, start, end)
