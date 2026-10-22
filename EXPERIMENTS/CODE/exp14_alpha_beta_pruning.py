import math

def alpha_beta_pruning(depth, node_index, is_max, values, alpha, beta, target_depth):
    if depth == target_depth:
        return values[node_index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta, target_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruning at depth {depth}, node {node_index} (Beta {beta} <= Alpha {alpha})")
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta, target_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruning at depth {depth}, node {node_index} (Beta {beta} <= Alpha {alpha})")
                break
        return best

terminal_scores = [3, 5, 6, 9, 1, 2, 0, -1]
target_depth = int(math.log2(len(terminal_scores)))

print("Terminal Leaf Nodes:", terminal_scores)
optimal = alpha_beta_pruning(0, 0, True, terminal_scores, -math.inf, math.inf, target_depth)
print(f"\nOptimal value with Alpha-Beta Pruning: {optimal}")
