'''
02.08 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
      beginning of the loop.

      DEFINITION

      Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
      as to make a loop in the linked list.

      EXAMPLE

      Input: A -> B -> C -> D -> E -> C -> D ...
      Output: C
'''

import sys

sys.path.insert(0, "/projetos/flask-test")

from Class_SinglyLinked import SinglyLinked

#Time: O(n) Space: O(n)
def DetectionLoop(ptr1):
    mark = set()
    while ptr1 != None:
        if ptr1 in mark:
            return ptr1.value
        mark.add(ptr1)
        ptr1 = ptr1.next
    return False
    
#Time: O(n) Space: O(1)
def Floyds_cycle_detection(LinkList: SinglyLinked):
    slow = fast = LinkList.startNode
    Check = False
    while (fast.next !=None and fast != None): 
        if fast == slow and Check:
            return slow.value
        if not Check:
            fast = fast.next.next
            slow = slow.next
        else:
            fast = fast.next
            slow = slow.next
        if fast == slow and not Check:
            Check = True
            fast = LinkList.startNode
    return False