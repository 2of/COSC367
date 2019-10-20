
def min_value(tree, alpha=float('-inf'), beta=float('inf')):
    if not isinstance(tree, list):
        return tree

    bestValue = float("inf")
    for i, node in enumerate(tree):
        currentValue = max_value(node, alpha, beta)
        bestValue = min(currentValue, bestValue)

        if currentValue <= alpha:
            if tree[i+1:]:
                print("Pruning:", ", ".join(map(str, tree[i+1:])))
            return currentValue

        beta = min(beta, currentValue)

    return bestValue

def max_value(tree, alpha=float('-inf'), beta=float('inf')):
    if not isinstance(tree, list):
        return tree

    bestValue = float("-inf")
    for i, node in enumerate(tree):
        currentValue = min_value(node, alpha, beta)
        bestValue = max(bestValue, currentValue)

        if currentValue >= beta:
            if tree[i + 1:]:
                print("Pruning:", ", ".join(map(str, tree[i+1:])))
            return currentValue

        alpha = max(alpha, currentValue)

    return bestValue

# no pruning when the root is max
# but one child pruned when the root is min
tree = [2, [-3, 1], 4, 1]
print("Game tree:", tree)
print("Computing the utility of the root as a max node...")
print("Root utility for maximiser:", max_value(tree))
print("Computing the utility of the root as a min node....")
print("Root utility for minimiser:", min_value(tree))

# # changing the order of children affects
# # what is being pruned.
# tree = [[3, 4], [1, 2]]
# print("Game tree:", tree)
# print("Computing the utility of the root as a max node...")
# print("Root utility for maximiser:", max_value(tree))
# print("Computing the utility of the root as a min node....")
# print("Root utility for minimiser:", min_value(tree))

# tree = [[2, 3, 4], [1, 100, -100]]
# print("Game tree:", tree)
# print("Computing the utility of the root as a max node...")
# print("Root utility for maximiser:", max_value(tree))
# print("Computing the utility of the root as a min node....")
# print("Root utility for minimiser:", min_value(tree))

# # From the lecture notes
# tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
# print("Game tree:", tree)
# print("Computing the utility of the root as a max node...")
# print("Root utility for maximiser:", max_value(tree))
# print("Computing the utility of the root as a min node....")
# print("Root utility for minimiser:", min_value(tree))

# tree = [[[3, 12], 8], [2, [4, 6]], [14, 5, 2]]
# print("Game tree:", tree)
# print("Computing the utility of the root as a max node...")
# print("Root utility for maximiser:", max_value(tree))
# print("Computing the utility of the root as a min node....")
# print("Root utility for minimiser:", min_value(tree))

# tree = [3, [[1, 2], [[4, 5], [6, 7]]], 8]
# print("Game tree:", tree)
# print("Computing the utility of the root as a max node...")
# print("Root utility for maximiser:", max_value(tree))
# print("Computing the utility of the root as a min node....")
# print("Root utility for minimiser:", min_value(tree))