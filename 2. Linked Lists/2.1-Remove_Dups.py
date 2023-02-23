'''
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list. 
FOLLOW UP 
How would you solve this problem if a temporary buffer is not allowed? 
'''
import sys

sys.path.insert(0, "/projetos/flask-test")

from Class_SinglyLinked import SinglyLinked

#Time: O(logn) Space: O(1)
def removeDups(linkedlist):
        ptr1 = ptr2 = list.startNode
        i = 0
        j = 0
        while (ptr1 != None):
            ptr2 = ptr1.next
            j = i + 1
            while (ptr2 != None):
                if ptr1.value == ptr2.value:
                    list.remove(j)
                ptr2 = ptr2.next
                j += 1
            i += 1
            ptr1 = ptr1.next