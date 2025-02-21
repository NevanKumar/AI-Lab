import networkx as nx
from queue import Queue

def bidirectional_bfs(graph, start, goal):
    if start == goal:
        return [start]

    forward_queue = Queue()
    backward_queue = Queue()

    forward_queue.put(start)
    backward_queue.put(goal)

    forward_visited = {start: None}
    backward_visited = {goal: None}

    while not forward_queue.empty() and not backward_queue.empty():
        if not forward_queue.empty():
            current_forward = forward_queue.get()
            for neighbor in graph.neighbors(current_forward):
                if neighbor not in forward_visited:
                    forward_visited[neighbor] = current_forward
                    forward_queue.put(neighbor)

                    if neighbor in backward_visited:
                        return construct_path(forward_visited, backward_visited, neighbor)

        if not backward_queue.empty():
            current_backward = backward_queue.get()
            for neighbor in graph.neighbors(current_backward):
                if neighbor not in backward_visited:
                    backward_visited[neighbor] = current_backward
                    backward_queue.put(neighbor)

                    if neighbor in forward_visited:
                        return construct_path(forward_visited, backward_visited, neighbor)

    return None

def construct_path(forward_visited, backward_visited, meeting_point):
    path = []
    current = meeting_point
    while current is not None:
        path.append(current)
        current = forward_visited[current]

    path.reverse()

    current = backward_visited[meeting_point]
    while current is not None:
        path.append(current)
        current = backward_visited[current]

    return path

def standard_bfs(graph, start, goal):
    queue = Queue()
    queue.put(start)
    visited = {start: None}

    while not queue.empty():
        current = queue.get()
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.put(neighbor)

    return None

def visualize_graph(graph, path):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)

if __name__ == "__main__":
    G = nx.Graph()
    edges = [
        ("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"),
        ("D", "E"), ("E", "F"), ("F", "G"), ("C", "G")
    ]
    G.add_edges_from(edges)

    start, goal = "A", "G"

    bidirectional_path = bidirectional_bfs(G, start, goal)
    print("Bi-directional BFS Path:", bidirectional_path)

    standard_path = standard_bfs(G, start, goal)
    print("Standard BFS Path:", standard_path)

    visualize_graph(G, bidirectional_path)
