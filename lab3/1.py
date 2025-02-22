import heapq
def manhattan_distance(x1, y1, x2, y2):
    """Calculate Manhattan distance between two points."""
    return abs(x1 - x2) + abs(y1 - y2)


def best_first_search(grid, start, goal):
    """Perform Best-First Search on the grid."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    priority_queue = []

    # Add start node to the priority queue
    start_x, start_y = start
    goal_x, goal_y = goal
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        _, (x, y) = heapq.heappop(priority_queue)

        # Check if we reached the treasure
        if (x, y) == goal:
            print(f"Treasure found at {x, y}")
            return True

        # Mark the current cell as visited
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 0:
                h = manhattan_distance(nx, ny, goal_x, goal_y)
                heapq.heappush(priority_queue, (h, (nx, ny)))

    print("Treasure not found!")
    return False


def get_user_input():
    """Get user input for grid setup."""
    # Grid size
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Initialize the grid
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Obstacles
    num_obstacles = int(input("Enter the number of obstacles: "))
    print("Enter obstacle positions as 'row col' (0-indexed):")
    for _ in range(num_obstacles):
        obs_x, obs_y = map(int, input().split())
        grid[obs_x][obs_y] = 1

    # Start position
    print("Enter the start position as 'row col':")
    start_x, start_y = map(int, input().split())

    # Goal position
    print("Enter the goal position as 'row col':")
    goal_x, goal_y = map(int, input().split())

    return grid, (start_x, start_y), (goal_x, goal_y)


# Main function
if __name__ == "__main__":
    print("Best-First Search: Find the Treasure!")
    grid, start, goal = get_user_input()
    print("\nGrid:")
    for row in grid:
        print(" ".join(map(str, row)))
    print(f"\nStart: {start}")
    print(f"Goal: {goal}")
    best_first_search(grid, start, goal)

