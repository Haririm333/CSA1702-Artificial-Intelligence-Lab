import math

def minimax(cur_depth, node_index, max_turn, scores, target_depth):
    if cur_depth == target_depth:
        return scores[node_index]

    if max_turn:
        return max(
            minimax(cur_depth + 1, node_index * 2, False, scores, target_depth),
            minimax(cur_depth + 1, node_index * 2 + 1, False, scores, target_depth)
        )
    else:
        return min(
            minimax(cur_depth + 1, node_index * 2, True, scores, target_depth),
            minimax(cur_depth + 1, node_index * 2 + 1, True, scores, target_depth)
        )

terminal_scores = [3, 5, 2, 9, 12, 5, 23, 23]
tree_depth = int(math.log2(len(terminal_scores)))

optimal_value = minimax(0, 0, True, terminal_scores, tree_depth)

print("Game Tree Terminal Node Values:")
print(terminal_scores)
print(f"Optimal Value evaluated by Minimax: {optimal_value}")
