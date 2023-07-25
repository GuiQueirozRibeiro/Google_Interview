'''
04.02 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
    algorithm to create a binary search tree with minimal height.
'''

class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def disp(self, nesting=0):
        indent = " " * nesting * 2
        output = f"{self.val}\n"
        if self.left is not None:
            output += f"{indent}L:"
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f"{indent}R:"
            output += self.right.disp(nesting + 1)
        return output

    def __str__(self):
        return self.disp()

# Time: O(n) Space: O(log n)
def array_to_binary_tree(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = Node(array[mid])
    root.left = array_to_binary_tree(array, start, mid - 1)
    root.right = array_to_binary_tree(array, mid + 1, end)
    return root