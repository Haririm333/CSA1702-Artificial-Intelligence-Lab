import heapq

def a_star_search(graph, heuristics, start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristics[start], 0, start, [start]))
    g_costs = {start: 0}
    closed_set = set()

    while open_set:
        f_cost, g_cost, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, g_cost

        if current in closed_set:
            continue
        closed_set.add(current)

        for neighbor, edge_weight in graph.get(current, []):
            tentative_g = g_cost + edge_weight

            if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g
                f = tentative_g + heuristics.get(neighbor, 0)
                heapq.heappush(open_set, (f, tentative_g, neighbor, path + [neighbor]))

    return None, float('inf')

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 5), ('E', 12)],
    'C': [('A', 4), ('F', 2)],
    'D': [('B', 5), ('G', 3)],
    'E': [('B', 12), ('G', 2)],
    'F': [('C', 2), ('G', 6)],
    'G': []
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 0
}

start_node = 'A'
goal_node = 'G'

path, cost = a_star_search(graph, heuristics, start_node, goal_node)

print(f"A* Shortest Path from {start_node} to {goal_node}:")
print(" -> ".join(path))
print(f"Total Path Cost: {cost}")
