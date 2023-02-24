'''
02.05 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
      digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a
      function that adds the two numbers and returns the sum as a linked list.

      EXAMPLE

      Input: (7 -> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
      Output: 2 -> 1 -> 9. That is, 912.

      FOLLOW UP

      Suppose the digits are stored in forward order. Repeat the above problem.

      EXAMPLE

      Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
      Output: 9 -> 1 -> 2. That is, 912.
'''

import sys

sys.path.insert(0, "/projetos/flask-test")

from Class_SinglyLinked import SinglyLinked
ListA = SinglyLinked()

#iterative - Time: O(A+B) Space: O(1)
def sumList(ListA: SinglyLinked, ListB: SinglyLinked):
    ptr1 = ListA.startNode
    ptr2 = ListB.startNode
    carry = 0
    soma = 0
    Bool = False
    if ListA.size > ListB.size:
        Bool = True
    while ptr1 !=None or ptr2 != None:
        if ptr1 == None:
            soma = ptr2.value + carry
        if ptr2 == None:
            soma = ptr1.value +carry
        if ptr1 != None and ptr2 != None:
            soma = ptr1.value + ptr2.value + carry
        carry = 0
        if soma > 9:
            carry = 1
            soma = soma%10
        if Bool:
            ptr1.value = soma
            ptr1 = ptr1.next
            if ptr2 != None:
                ptr2 = ptr2.next
        else:
            ptr2.value = soma
            ptr2 = ptr2.next
            if ptr1 != None:
                ptr1 = ptr1.next
    if Bool:
        return ListA
    return ListB

#recursive - Time: O(max(A+B)) Space: O(1)
def Size(ListA: SinglyLinked, ListB: SinglyLinked):
    x = abs(ListA.size - ListB.size)
    size = ListA.size 
    for _ in range(x):
        if ListA.size > ListB.size: 
            ListB.add(0, 0)
        if ListB.size > ListA.size:
            size = ListB.size 
            ListA.add(0, 0)
    return recList(ListA.startNode, ListB.startNode, size)

def recList(ptr1, ptr2, size):
    Sum = 0
    if ptr1 == None:
        return 0
    carry = recList(ptr1.next, ptr2.next, size)
    Sum = ptr1.value + ptr2.value + carry
    carry = 0
    if Sum > 9:
        carry = 1
        Sum = Sum%10
    if ptr1 == ListA.startNode:
        ptr1.value = Sum
        if carry == 1:
            ListA.add(0,1)
        return ListA
    else:
        ptr1.value = Sum
        return carry