'''
04.11 Random Node: You are implementing a binary tree class from scratch which, in addition to
    insert, find, and delete, has a method getRandomNode() which returns a random node
    from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
    for getRandomNode, and explain how you would implement the rest of the methods.
'''

import random


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.size = 1

    @property
    def left_size(self):
        if self.left:
            return self.left.size
        return 0

    @property
    def right_size(self):
        if self.right:
            return self.right.size
        return 0


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Time: O(log n) Space: O(log n)
    def insert(self, key):
        new = Node(key)
        if self.root is None:
            self.root = new
            return

        current = self.root
        while current:
            current.size += 1
            if current.key >= key:
                if current.left is None:
                    current.left = new
                    new.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    new.parent = current
                    return
                current = current.right

    # Time: O(log n) Space: O(log n)
    def delete(self, node, key):

        if node is None:
            return node

        if key < node.key:
            node.left = self.delete_helper(node.left, key)

        elif key > node.key:
            node.right = self.delete_helper(node.right, key)

        else:
            if node.left is None:
                temp, node = node.right, None
                return temp

            elif node.right is None:
                temp, node = node.left, None
                return temp

            temp = min_val_node(node.right)
            node.key = temp.key
            node.right = self.delete_helper(node.right, temp.key)

        node.size -= 1
        return node

    # Time: O(log n) Space: O(1)
    def get_node(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current

            if current.key > key:
                current = current.left
            else:
                current = current.right
        raise Exception("No such value in the tree")

    # Time: O(log n) Space: O(1)
    def get_random_node(self):
        current = self.root
        # with probability 1/N = 1/(1+l+r) return node
        # with probability l/N go down left
        # with probability r/N go down right

        while current:
            choices = ["self", "left", "right"]
            choice_weights = [1, current.left_size, current.right_size]
            decision = random.choices(choices, choice_weights)[0]

            if decision == "self":
                return current

            if decision == "left":
                current = current.left
            elif decision == "right":
                current = current.right
            else:
                raise RuntimeError("Should not be possible")


def min_val_node(node):
    current = node
    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current