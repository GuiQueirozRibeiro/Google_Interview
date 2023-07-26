'''
04.06 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
    binary search tree. You may assume that each node has a link to its parent.
'''

# Time: O(n) Space: O(1)
def in_order_successor(input_node):
    if input_node is None:
        return None

    if input_node.right:
        current = input_node.right
        while current.left:
            current = current.left
        return current

    ancestor = input_node.parent
    child = input_node
    while ancestor and ancestor.right == child:
        child = ancestor
        ancestor = ancestor.parent
    return ancestor