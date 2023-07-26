'''
04.03 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
    at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
'''

from collections import deque

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class SinglyLinked:
    def __init__(self):
        self.startNode = Node(None, None)
        self.size = 0

    # Time: O(n) Space: O(1)
    def add(self, index, value):
        if (index < 0 or index > self.size):
            return "ERROR: invalid index"

        if self.startNode.value == None:
            self.startNode.value = value

        elif index == 0:
            newNode = Node(value, self.startNode)
            self.startNode = newNode

        else:
            current = self.startNode
            for _ in range(index-1):
                current = current.next

            newNode = Node(value, current.next)
            current.next = newNode

        self.size += 1

    # Time: O(1) Space: O(1)
    def pop_head(self):
        if self.size == 0:
            return None

        head_to_pop = self.startNode
        self.startNode = self.startNode.next
        self.size -= 1
        return head_to_pop

class BinaryNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

# Time: O(n) Space: O(n)
def create_node_list_by_depth(tree_root):
    levels = {}
    q = deque()
    q.append((tree_root, 0))

    while len(q) > 0:
        node, level = q.popleft()
        if level not in levels:
            levels[level] = SinglyLinked()
        levels[level].add(node)

        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    return levels

# Time: O(n) Space: O(n)
def create_node_list_by_depth_b(tree):
    if not tree:
        return []

    curr = tree
    result = [SinglyLinked([curr])]
    level = 0

    while result[level]:
        result.append(SinglyLinked())
        for linked_list_node in result[level]:
            n = linked_list_node.value
            if n.left:
                result[level + 1].add(n.left)
            if n.right:
                result[level + 1].add(n.right)
        level += 1
    return result
