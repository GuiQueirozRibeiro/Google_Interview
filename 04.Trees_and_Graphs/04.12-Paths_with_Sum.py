'''
04.12 Paths with Sum: You are given a binary tree in which each node contains an integer value (which
    might be positive or negative). Design an algorithm to count the number of paths that sum to a
    given value. The path does not need to start or end at the root or a leaf, but it must go downwards
    (traveling only from parent nodes to child nodes).
'''

from Binary_Tree import BinaryTree

# Brute Force O(n log n)
def count_sum_paths(tree, target):
    if not isinstance(tree, BinaryTree):
        return None
    return _count_sum_paths(tree.root, target)


def _count_sum_paths(node, target_sum):
    if not node:
        return 0
    return (
        pathsfrom(node, target_sum)
        + _count_sum_paths(node.left, target_sum)
        + _count_sum_paths(node.right, target_sum)
    )


def pathsfrom(node, target_sum):
    if not node:
        return 0
    target_sum -= node.key
    counter = 0
    if target_sum == 0:
        counter += 1
    return (
        counter + pathsfrom(node.left, target_sum) + pathsfrom(node.right, target_sum)
    )


# Optimized O(n)
def count_sum_paths_optimized(tree, target_sum):
    if not isinstance(tree, BinaryTree):
        return None
    return _count_sum_paths_optimizied(tree.root, target_sum)


def _count_sum_paths_optimizied(node, target_sum, running=0, hashtable=None):
    if hashtable is None:
        hashtable = {}
    if not node:
        return 0
    running += node.key
    total = hashtable.get(running - target_sum, 0)
    if running == target_sum:
        total += 1
    increment(hashtable, running, 1)
    left_count = _count_sum_paths_optimizied(node.left, target_sum, running, hashtable)
    right_count = _count_sum_paths_optimizied(
        node.right, target_sum, running, hashtable
    )
    total += left_count + right_count
    increment(hashtable, running, -1)
    return total


def increment(hashmap, key, delta):
    hashmap.setdefault(key, 0)
    hashmap[key] += delta
    if hashmap[key] == 0:
        hashmap.pop(key)
