'''
03.04 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
'''

from Class_Stack import Stack

class MyQueue:
    def __init__(self):
        self.new_stack = Stack()
        self.old_stack = Stack()

    # Time: O(n) Space: O(n)
    def _shift_stacks(self):
        if self.old_stack.is_empty():
            while not self.new_stack.is_empty():
                self.old_stack.push(self.new_stack.pop())

    # Time: O(1) Space: O(1)
    def add(self, value):
        return self.new_stack.push(value)

    # Time: O(1) Space: O(n)
    def peek(self):
        if self.is_empty():
            return False
        self._shift_stacks()
        return self.old_stack.peek()

    # Time: O(1) Space: O(n)
    def remove(self):
        if self.is_empty():
            return False
        self._shift_stacks()
        return self.old_stack.pop()

    # Time: O(1) Space: O(1)
    def is_empty(self):
        return len(self) == 0

    # Time: O(1) Space: O(1)
    def __len__(self):
        return len(self.new_stack) + len(self.old_stack)