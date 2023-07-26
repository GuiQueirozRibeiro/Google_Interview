'''
02.04 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.

    EXAMPLE

    Input: 3 -> 5 -> 8 -> 5 - > 10 -> 2 -> 1 [partition = 5)
    Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''

# Time: O(n) Space: O(1)
def partition(linklist, x):
    ptr1 = ptr2 = list.startNode
    runner = 0  
    while ptr2 != None: 
        if ptr1.value < x:
            ptr1 = ptr1.next
        elif ptr2.value < x:
            runner = ptr1.value
            ptr1.value = ptr2.value
            ptr2.value = runner
            ptr1 = ptr1.next
        ptr2 = ptr2.next      
    return list