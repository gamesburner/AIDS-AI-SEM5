graph = {
    "6": ["3", "7"],
    "3": ["1"],
    "7": ["4"],
    "1": [],
    "4": []
}

def bfs(graph, start_node):
    visited = []
    queue = []

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)



print("BFS search")
bfs(graph, "6")
