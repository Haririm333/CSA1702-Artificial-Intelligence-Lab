import itertools

def travelling_salesman(distance_matrix, cities):
    n = len(cities)
    start_city = 0
    other_cities = list(range(1, n))

    min_cost = float('inf')
    best_path = None

    for perm in itertools.permutations(other_cities):
        current_path = [start_city] + list(perm) + [start_city]
        current_cost = 0

        for i in range(len(current_path) - 1):
            current_cost += distance_matrix[current_path[i]][current_path[i + 1]]

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    named_path = [cities[i] for i in best_path]
    return named_path, min_cost

cities = ["City A", "City B", "City C", "City D"]

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_tour, min_distance = travelling_salesman(distance_matrix, cities)

print("Optimal TSP Tour:")
print(" -> ".join(best_tour))
print(f"Minimum Distance: {min_distance}")
