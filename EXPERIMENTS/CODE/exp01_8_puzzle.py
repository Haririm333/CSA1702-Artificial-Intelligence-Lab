import heapq

GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

MOVES = [(-1, 0, 'UP'), (1, 0, 'DOWN'), (0, -1, 'LEFT'), (0, 1, 'RIGHT')]

def manhattan_distance(state):
    distance = 0
    goal_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 0: (2, 2)
    }
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                gr, gc = goal_positions[val]
                distance += abs(r - gr) + abs(c - gc)
    return distance

def find_blank(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c
    return None

def get_neighbors(state):
    neighbors = []
    r, c = find_blank(state)
    for dr, dc, move_name in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            state_list = [list(row) for row in state]
            state_list[r][c], state_list[nr][nc] = state_list[nr][nc], state_list[r][c]
            new_state = tuple(tuple(row) for row in state_list)
            neighbors.append((new_state, move_name))
    return neighbors

def solve_8_puzzle(start_state):
    counter = 0
    pq = []
    h = manhattan_distance(start_state)
    heapq.heappush(pq, (h, 0, counter, start_state, []))
    visited = {start_state: 0}

    while pq:
        f, g, _, current_state, path = heapq.heappop(pq)
        if current_state == GOAL_STATE:
            return path
        for next_state, move in get_neighbors(current_state):
            new_g = g + 1
            if next_state not in visited or new_g < visited[next_state]:
                visited[next_state] = new_g
                new_f = new_g + manhattan_distance(next_state)
                counter += 1
                heapq.heappush(pq, (new_f, new_g, counter, next_state, path + [(move, next_state)]))
    return None

def print_board(state):
    for row in state:
        print(" ".join(str(x) if x != 0 else "_" for x in row))
    print()

start_state = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

print("Initial State:")
print_board(start_state)

print("Goal State:")
print_board(GOAL_STATE)

solution = solve_8_puzzle(start_state)
if solution is not None:
    print(f"Solved in {len(solution)} steps:\n")
    for step, (move, next_state) in enumerate(solution, 1):
        print(f"Step {step}: {move}")
        print_board(next_state)
else:
    print("No solution found.")
