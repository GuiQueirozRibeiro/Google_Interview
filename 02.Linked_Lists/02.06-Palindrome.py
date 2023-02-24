'''
02.06 Palindrome: Implement a function to check if a linked list is a palindrome.
'''

import sys

sys.path.insert(0, "/projetos/flask-test")

from Class_SinglyLinked import SinglyLinked

#Time: O(n) Space: O(n)
def Ptr1(ptr1, ptr2):
    i = 0
    while ptr2.next != None:
        i += 1
        if list.size//2 + 1 == i:
            ptr1 = None
            ptr2.next = None
        else:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
    return ptr1

def Palindrome(ptr2):
    if ptr2 == None:
        return True
    check = Palindrome(ptr2.next)
    if check == False:
        return False
    ptr1 = list.startNode
    ptr1 = Ptr1(ptr1, ptr2)
    if ptr1 == None:
        return True   
    else:
        current = ptr1.value == ptr2.value
    return current