def is_valid(region, color, assignment, neighbors):
    for neighbor in neighbors.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(regions, colors, neighbors, assignment=None):
    if assignment is None:
        assignment = {}

    if len(assignment) == len(regions):
        return assignment

    unassigned = [r for r in regions if r not in assignment]
    first_region = unassigned[0]

    for color in colors:
        if is_valid(first_region, color, assignment, neighbors):
            assignment[first_region] = color
            result = map_coloring(regions, colors, neighbors, assignment)
            if result is not None:
                return result
            del assignment[first_region]

    return None

regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
colors = ['Red', 'Green', 'Blue']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

solution = map_coloring(regions, colors, neighbors)

if solution:
    print("Map Coloring CSP Solution:")
    for region, color in sorted(solution.items()):
        print(f"{region:4} -> {color}")
else:
    print("No valid coloring found.")
