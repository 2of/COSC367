

import sys
import math

''' Remember that we are reading 'one line down' 
when looking for the index, hence swap the read head'''

def max_action_value(tree):
    if type(tree) is int:
        return(None, tree)
    mindex = -1
    val = float("-inf")
    for cand in range(len(tree)):
        this = min_action_helper_value(tree[cand])

        if this > val:
            val = this
            mindex = cand
    return (mindex, val)


def min_action_value(tree):
    if type(tree) is int:
        return(None, tree)
    mindex = -1
    val = float("inf")
    for cand in range(len(tree)):
        this = max_action_helper_value(tree[cand])
        if this < val:
            val = this
            mindex = cand
    return (mindex, val)


def max_action_helper_value(tree):
    if type(tree) is int:
        return tree
    return max([min_action_helper_value(tree[a]) for a in range(len(tree))])


def min_action_helper_value(tree):
    if type(tree) is int:
        return tree
    return min([max_action_helper_value(tree[a]) for a in range(len(tree))])


game_tree = [2, [-3, 1], 4, 1]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print("----")
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)


game_tree = 3

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

game_tree = [1, 2, [3]]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)


game_tree = [[[3, 12], 8], [2, [4, 6]], [14, 5, 2]]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)


game_tree = [
    [[7, -5, 3, 1], [-5, 4, -10, 3], [-10, 6, 8, -5]],
    [[9, 2, -8, 1], [-1, -6, -10, 7], [-3, -2, -3, -2]],
    [[-5, -6, 5]],
]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)


sys.exit()
