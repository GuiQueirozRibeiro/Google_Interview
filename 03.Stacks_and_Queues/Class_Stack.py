class Stack:
    def __init__(self):
        self.items = []

    # Time complexity: O(1)
    def is_empty(self):
        return len(self.items) == 0

    # Time complexity: O(1)
    def push(self, item):
        self.items.append(item)

    # Time complexity: O(1)
    def pop(self):
        return self.items.pop()

    # Time complexity: O(1)
    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    # Time complexity: O(1)
    def __len__(self):
        return len(self.items)

    # Time complexity: O(1)
    def __bool__(self):
        return bool(self.items)