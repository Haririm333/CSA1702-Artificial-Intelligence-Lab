from collections import deque

def water_jug_problem(cap1, cap2, target):
    visited = set()
    queue = deque()
    queue.append(((0, 0), []))
    visited.add((0, 0))

    while queue:
        (j1, j2), path = queue.popleft()

        if j1 == target or j2 == target:
            return path + [(j1, j2)]

        next_states = [
            ((cap1, j2), "Fill Jug 1"),
            ((j1, cap2), "Fill Jug 2"),
            ((0, j2), "Empty Jug 1"),
            ((j1, 0), "Empty Jug 2"),
            ((j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)), "Pour Jug 1 -> Jug 2"),
            ((j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1)), "Pour Jug 2 -> Jug 1")
        ]

        for state, action in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(j1, j2, action)]))

    return None

cap1, cap2, target = 4, 3, 2
solution = water_jug_problem(cap1, cap2, target)

if solution:
    print(f"Steps to measure {target} liters using jugs of capacity {cap1} and {cap2}:\n")
    for step in solution[:-1]:
        print(f"Jug1: {step[0]}, Jug2: {step[1]}  ->  Action: {step[2]}")
    final_state = solution[-1]
    print(f"Jug1: {final_state[0]}, Jug2: {final_state[1]}  ->  Target Reached!")
else:
    print("No solution possible.")
