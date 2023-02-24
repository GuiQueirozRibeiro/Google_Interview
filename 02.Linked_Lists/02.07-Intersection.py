'''
02.07 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
      Note that the intersection is defined based on reference, not value. That is, if the kth
      node of the first linked list is the exact same node (by reference) as the jth node of the second
      linked list, then they are intersecting.
'''

import sys

sys.path.insert(0, "/projetos/flask-test")

from Class_SinglyLinked import SinglyLinked

#Time: O(A+B) Space: O(1)
def intersection(ListA, ListB):
    ptr1 = ListA.startNode
    ptr2 = ListB.startNode
    j = abs(ListA.size - ListB.size)
    if ListA.size > ListB.size:
        for _ in range(j):
            ptr1 = ptr1.next
    else:
        for _ in range(j):
            ptr2 = ptr2.next
    while ptr1!= None:
        if ptr1 == ptr2:
            return ptr1.value
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return False