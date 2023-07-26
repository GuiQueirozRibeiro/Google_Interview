'''
04.04 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
    this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
    node never differ by more than one.
'''

class BinaryNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

# Time: O(n) Space: O(n)
def find_max_depth(node, level=0):
    if node is None:
        return level
    if not node.left:
        return find_max_depth(node.right, level + 1)
    if not node.right:
        return find_max_depth(node.left, level + 1)
    return max(
        find_max_depth(node.left, level + 1), find_max_depth(node.right, level + 1)
    )

# Time: O(n) Space: O(n)
def find_min_depth(node, level=0):
    if node is None:
        return level
    if not node.left:
        return find_min_depth(node.right, level + 1)
    if not node.right:
        return find_min_depth(node.left, level + 1)
    return min(
        find_min_depth(node.left, level + 1), find_min_depth(node.right, level + 1)
    )


# Version 1:
# Find the max tree depth and min tree depth independently.
# Then compare their values.
# Time: O(n) Space: O(n)
def is_balanced_v1(node):
    return find_max_depth(node) - find_min_depth(node) < 2


# Alternative Recursive Approach
# Time: O(n) Space: O(n)
def _find_height(root):
    if root is None:
        return 0
    left_height = _find_height(root.left)
    if left_height == -1:
        return -1

    right_height = _find_height(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1


# Version 2:
# Traverse the tree and track the largest and smallest depth of each leaf node.
# Then compare the largest and smallest depth.
# Time: O(n) Space: O(n)
def is_balanced_v2(node):
    min_depth = 10**100
    max_depth = -(10**100)
    queue = [(node, 0)]
    visited = [node]

    while len(queue) > 0:
        curr_node, curr_depth = queue.pop(0)

        if curr_node.left is None and curr_node.right is None:
            if curr_depth > max_depth:
                max_depth = curr_depth
            if curr_depth < min_depth:
                min_depth = curr_depth
        else:
            if curr_node.left and curr_node.left not in visited:
                visited.append(curr_node.left)
                queue.append((curr_node.left, curr_depth + 1))
            if curr_node.right and curr_node.right not in visited:
                visited.append(curr_node.right)
                queue.append((curr_node.right, curr_depth + 1))

    return max_depth - min_depth < 2


# Time: O(n) Space: O(n)
def is_balanced_v3(root):
    return _find_height(root) > -1