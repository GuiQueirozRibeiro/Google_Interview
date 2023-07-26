'''
04.1O Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
    algorithm to determine if T2 is a subtree of T1.
    A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
    That is, if you cut off the tree at node n, the two trees would be identical.
'''

from Binary_Tree import BinaryTree, Node


class ComparableTreeNode(Node):
    def __eq__(self, other):
        if not isinstance(other, ComparableTreeNode):
            return False
        return (
            self.key == other.key
            and self.left == other.left
            and self.right == other.right
        )


class ComparableBinaryTree(BinaryTree):
    NodeCls = ComparableTreeNode


# "needle in a haystack"
# haystack == the thing we're searching inside
# needle == the thing we're looking for
# Time: O(m*n) Space: O(m+n)
def is_subtree(haystack_tree, needle_tree):
    if not haystack_tree or not needle_tree:
        return False
    return _is_subtree(haystack_tree.root, needle_tree.root)

# Time: O(m*n) Space: O(m+n)
def _is_subtree(haystack_node, needle_node):
    if haystack_node is None or needle_node is None:
        return False
    if haystack_node == needle_node:
        return True

    return _is_subtree(haystack_node.left, needle_node) or _is_subtree(
        haystack_node.right, needle_node
    )
