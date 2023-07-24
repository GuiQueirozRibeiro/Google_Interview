'''
03.05 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
    an additional temporary stack, but you may not copy the elements into any other data structure
    (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
'''

from Class_Stack import Stack

class SortedStack(Stack):
    def __init__(self):
        super().__init__()
        self.temp_stack = Stack()

    # Time complexity: O(n)
    def push(self, item):
        if self.is_empty() or item < self.peek():
            super().push(item)
        else:
            while self.peek() is not None and item > self.peek():
                self.temp_stack.push(self.pop())
            super().push(item)
            while not self.temp_stack.is_empty():
                super().push(self.temp_stack.pop())
