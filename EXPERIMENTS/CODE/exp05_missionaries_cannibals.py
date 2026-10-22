from collections import deque

def is_valid(m, c):
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    m_right = 3 - m
    c_right = 3 - c
    if m_right > 0 and m_right < c_right:
        return False
    return True

def get_successors(state):
    m, c, boat = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    successors = []

    for dm, dc in moves:
        if boat == 1:
            nm, nc = m - dm, c - dc
            n_boat = 0
            action = f"Cross {dm}M and {dc}C to Right"
        else:
            nm, nc = m + dm, c + dc
            n_boat = 1
            action = f"Cross {dm}M and {dc}C to Left"

        if is_valid(nm, nc):
            successors.append(((nm, nc, n_boat), action))

    return successors

def solve_missionaries_cannibals():
    start_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    queue = deque([(start_state, [])])
    visited = {start_state}

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path + [(state, "Goal Reached")]

        for next_state, action in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(state, action)]))

    return None

solution = solve_missionaries_cannibals()

if solution:
    print("Missionaries and Cannibals Solution Steps:\n")
    for step, (state, action) in enumerate(solution):
        m, c, b = state
        boat_side = "Left" if b == 1 else "Right"
        print(f"Step {step}: Left Bank: ({m}M, {c}C), Right Bank: ({3-m}M, {3-c}C), Boat: {boat_side} -> {action}")
else:
    print("No solution found.")
