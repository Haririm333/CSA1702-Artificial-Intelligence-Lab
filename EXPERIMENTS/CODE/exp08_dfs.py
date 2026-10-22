def dfs_recursive(graph, node, visited=None, traversal=None):
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []

    visited.add(node)
    traversal.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal)

    return traversal

def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'

print("DFS Recursive Traversal:")
print(" -> ".join(dfs_recursive(graph, start)))

print("\nDFS Iterative Traversal:")
print(" -> ".join(dfs_iterative(graph, start)))
