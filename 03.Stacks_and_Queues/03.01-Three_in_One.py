'''
03.01 Three in One: Describe how you could use a single array to implement three stacks.
'''

class MultiStack:
    def __init__(self, stack_size, number_of_stacks):
        self.number_of_stacks = number_of_stacks
        self.array = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks
        self.stack_size = stack_size

    # Time complexity: O(1)
    def push(self, value, stack_num):
        if self.is_full(stack_num):
            raise ValueError(f"Push failed: stack #{stack_num} is full")
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value

    # Time complexity: O(1)
    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise ValueError(f"Cannot pop from empty stack #{stack_num}")
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value

    # Time complexity: O(1)
    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise ValueError(f"Cannot peek at empty stack #{stack_num}")
        return self.array[self.index_of_top(stack_num)]

    # Time complexity: O(1)
    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    # Time complexity: O(1)
    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    # Time complexity: O(1)
    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1