from collections import deque


def bfs(maze, start, end):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], len(visited)

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < len(maze) and
                    0 <= neighbor[1] < len(maze[0]) and
                    maze[neighbor[0]][neighbor[1]] == 1 and
                    neighbor not in visited):
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    return None, len(visited)


def dfs(maze, start, end):
    stack = [start]
    visited = set([start])
    parent = {start: None}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while stack:
        current = stack.pop()
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], len(visited)

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < len(maze) and
                    0 <= neighbor[1] < len(maze[0]) and
                    maze[neighbor[0]][neighbor[1]] == 1 and
                    neighbor not in visited):
                stack.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    return None, len(visited)


# Example Usage:
maze = [
    [1, 0, 1, 1],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]
start = (0, 0)
end = (3, 3)

bfs_path, bfs_nodes = bfs(maze, start, end)
dfs_path, dfs_nodes = dfs(maze, start, end)

print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)
print("BFS Nodes Explored:", bfs_nodes)
print("DFS Nodes Explored:", dfs_nodes)

