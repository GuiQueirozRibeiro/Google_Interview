''' 
02.02 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
'''

import sys

sys.path.insert(0, "/projetos/flask-test")

from Class_SinglyLinked import SinglyLinked

# Time: O(n) Space: O(1)
def recursiveElement(node, k):
    if node == None:
        return -1
    i = recursiveElement(node.next, k)
    i += 1
    if i == k:
        print(node.value)
    return i