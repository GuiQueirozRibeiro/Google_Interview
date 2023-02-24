class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def updateValue(self, value):
        self.value = value

    def updateNext(self, next):
        self.next = next

class SinglyLinked:
    def __init__(self):
        self.startNode = Node(None, None)
        self.size = 0

    def add(self, index, value):
        if (index < 0 or index > self.size):
            return "ERROR: invalid index"

        if self.startNode.value == None:
            self.startNode.updateValue(value)

        elif index == 0:
            newNode = Node(value, self.startNode)
            self.startNode = newNode

        else:
            current = self.startNode

            for _ in range(index-1):
                current = current.next

            newNode = Node(value, current.next)
            current.next = newNode
            
        self.size += 1

    def remove(self, index):
        if (index < 0 or index > self.size):
            return "ERROR: invalid index"
        elif self.size == 0:
            return "ERROR: empty list"
        elif index == 0:
            self.startNode = self.startNode.next
        else:
            current = self.startNode

            for _ in range(index-1):
                current = current.next

            current.next = current.next.next
        
        self.size -= 1

    def search(self, index):
        if (index < 0 or index > self.size-1):
            return "ERROR: invalid index"

        current = self.startNode

        for _ in range(index):
            current = current.next

        return current
    
    def addList(self, index: int, list):
        for i, el in enumerate(list):
            self.add(index+i, el)

    def __str__(self):
        string = [0 for _ in range(self.size)]
        
        current = self.startNode
        for i in range(self.size):
            string[i] = str(current.value)
            current = current.next
            
        return ''.join(string)
    
    def addNode(self, index: int, node: Node):
        if (index < 0 or index > self.size):
            return "[ERROR]: invalid index"
        
        if self.startNode.value == None or index == 0:
            self.startNode = node
            current = self.startNode
            size = 1
            while current.next:
                size += 1
                current = current.next
            self.size = size
        
        else:
            current = self.startNode

            for _ in range(index-1):
                current = current.next
            
            prevCurrentNext = current.next
            current.next = node
            current = node
            size = 1
            while current.next:
                size += 1
                current = current.next
        
            current.next = prevCurrentNext
            self.size += size