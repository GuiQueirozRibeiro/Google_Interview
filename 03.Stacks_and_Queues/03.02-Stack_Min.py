'''
03.02 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
    which returns the minimum element? Push, pop and min should all operate in O(1) time.
'''

from Class_Stack import Stack

class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.minvals = Stack()

    # Time: O(1) Space: O(1)
    def push(self, value):
        super().push(value)
        if not self.minvals or value <= self.minimum():
            self.minvals.push(value)

    # Time: O(1) Space: O(1)
    def pop(self):
        value = super().pop()
        if value == self.minimum():
            self.minvals.pop()
        return value
  
    # Time: O(1) Space: O(1)
    def minimum(self):
        return self.minvals.peek()