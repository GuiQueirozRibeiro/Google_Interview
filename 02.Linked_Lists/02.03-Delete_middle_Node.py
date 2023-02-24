'''
02.03 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
      the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
      that node.

      EXAMPLE

      Input: the node c from the linked list a -> b -> c -> d -> e -> f
      Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
'''

import sys

sys.path.insert(0, "/projetos/flask-test")

from Class_SinglyLinked import SinglyLinked

#Time: O(n) Space: O(1)
def removeMiddle(linklistm, k):
    middle = list.search(k)
    while middle != None:
        if middle.next == None:
            middle = None
            list.size -= 1
        else:
            middle.value = middle.next.value
            middle = middle.next