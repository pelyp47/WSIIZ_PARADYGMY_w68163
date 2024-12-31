def bfs_shortest_path(graph, start, goal):
    if start == goal:
        return [start]

    queue = [[start]]

    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            visited.append(node)
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                newPath = path + [neighbor]
                queue.append(newPath)
                if neighbor == goal:
                    return newPath
    return []

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

startNode = 'A'
goalNode = 'F'

shortestPath = bfs_shortest_path(graph, startNode, goalNode)
print(shortestPath)