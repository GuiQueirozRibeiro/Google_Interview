class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def updateValue(self, value):
        self.value = value

    def updateNext(self, next):
        self.next = next

class Stack:
    def __init__(self):
        self.top = Node(None, None)
        self.min = Node(None, None)
        self.size = 0
    
    def pop(self):
        if not self.isEmpty():
            if self.top.value == self.min.value:
                self.min = self.min.next        
            prevTop = self.top
            self.top = self.top.next
            self.size -= 1
            return prevTop
        else:
            return "Stack is empty"
    
    def push(self, value):
        if not self.isEmpty():
            node = Node(value, None)
            if self.min.value > node.value:
                self.min = Node(value, self.min)
            node.next = self.top
            self.top = node
            self.size += 1
            
        else:
            node = Node(value, None)
            self.min = Node(value, None)
            node.next = self.top
            self.top = node
            self.size += 1
            
    def minimun(self):
        if not self.isEmpty():
            return self.min.value
        else:
            return "Stack is empty"
    
    def peek(self):
        return self.top.value
    
    def isEmpty(self):
        return self.size == 0
    
    def __str__(self):
        string = "Top "
        cur = self.top
        while cur.value != None:
            if cur.next.value == None:
                string += "Bottom "
            string += str(cur) + "\n"
            cur = cur.next
        return string

class Queue:
    def __init__(self):
        self.start = Node(None, None)
        self.end = self.start
        self.size = 0
    
    def remove(self):
        if not self.isEmpty():
            prevStart = self.start
            self.start = self.start.next
            self.size -= 1
            return prevStart
        else:
            return "Stack is empty"
    
    def add(self, value):
        if self.start.value == None:
            node = Node(value, None)
            self.start = self.end = node
        else:
            if self.start == self.end:
                node = Node(value, None)
                self.start.next = self.end = node
            else:
                node = Node(value, None)
                self.end.next = node
                self.end = self.end.next
        self.size += 1
    
    def peek(self):
        return self.end.value
    
    def isEmpty(self):
        return self.size == 0
    
    def __str__(self):
        string = "Top "
        cur = self.start
        while cur.value != None:
            if cur.next.value == None:
                string += "Bottom "
            string += str(cur) + "\n"
            cur = cur.next
        return string

'''
Three in One: Describe how you could use a single array to implement three stacks. 
Hints: #2, #72, #38, #58 
'''

class StackArray:
    def _init_(self, size):
        if size < 3:
            raise ValueError("Array should have at least a length of 3.")
        self.array = [None for _ in range(size)]
        
        div = size // 3
        rest = size % 3

        self.stacks = [0, 0, 0]
        startIndex = 0
        for i in range(3):
            if rest > 0:
                self.stacks[i] = {"size": div + 1, "start": startIndex}
                rest -= 1
            else:
                self.stacks[i] = {"size": div, "start": startIndex}
            startIndex += self.stacks[i]["size"]
        
        print(self.stacks)

        self.stack1 = Stack(self.stacks[0]["size"], self.stacks[0]["start"], self.array)
        self.stack2 = Stack(self.stacks[1]["size"], self.stacks[1]["start"], self.array)
        self.stack3 = Stack(self.stacks[2]["size"], self.stacks[2]["start"], self.array)
        
    def _str_(self):
        return str(self.array)
        
class stackArray:
    def _init_(self, size, start, array):
        self.fixedSize = size
        self.size = 0
        self.start = start
        self.end = array[self.start]
        self.array = array
        
    def isEmpty(self):
        return self.size == 0
    
    def pop(self):
        if not self.isEmpty():
            self.array[self.start + self.size - 1] = None
            self.size -= 1
            if not self.isEmpty():
                self.end = self.array[self.start + self.size - 1]
            else:
                self.end = self.array[self.start]
                
    def push(self,value):
        if self.size == self.fixedSize:
            raise MemoryError("Cannot grow stack further.")
        else:
            self.array[self.start + self.size] = value
            self.size += 1

class StackPlates:
   def __init__(self, capacity):
       if capacity < 1:
            raise ValueError("a stack is greater than one")
       else:   
           self.capacity = capacity
           self.size = 0
           self.top = Node(None, None)
           self.stacks

def Print(ptr1):
    while(ptr1 != None):
        if ptr1.value == None:
            ptr1 = ptr1.next
        else:
            print(ptr1.value)
            ptr1 = ptr1.next

stack = Stack()
File = Queue()

print(stack.isEmpty())

stack.push(7)
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(1)

print(stack.isEmpty())
print(stack.peek())
print()

print(stack.minimun())
stack.pop()
print(stack.minimun())

print()

Print(stack.top)

#Print(stack.top)

print()
#----------------------------------------

print(File.isEmpty())

File.add(1)
File.add(2)
File.add(3)
File.add(4)
File.add(7)

print(File.isEmpty())
print(File.peek())
print()

Print(File.start)

File.remove()

print()

'''
push
    - verifica se o tamanho se esgotou, caso sim será criado uma nova stack que deve se relacionar com a anterior

criar novo parametro
    - Node = (value, next, stack number; ex: 1, 2, 3, 4)

entao caso o tamanho se esgote o no é criado com o stack number += 1

pop
    - quando chegar ao último elemento, subtrai o stack number -= 1
'''