'''
03.06 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
    out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
    or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
    that type). They cannot select which specific animal they would like. Create the data structures to
    maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
    and dequeueCat. You may use the built-in Linked list data structure.
'''

import time

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class SinglyLinked:
    def __init__(self):
        self.startNode = Node(None, None)
        self.size = 0

    # Time: O(n) Space: O(1)
    def add(self, index, value):
        if (index < 0 or index > self.size):
            return "ERROR: invalid index"

        if self.startNode.value == None:
            self.startNode.value = value

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

    # Time: O(1) Space: O(1)
    def pop_head(self):
        if self.size == 0:
            return None

        head_to_pop = self.startNode
        self.startNode = self.startNode.next
        self.size -= 1
        return head_to_pop

class Animal:
    def __init__(self, name):
        self.time_admitted = time.time()
        self.name = name

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class AnimalShelter(SinglyLinked):
    # Time: O(n) Space: O(1)
    def enqueue(self, animal):
        animal_node = Node(animal, None)
        self.add(self.size, animal_node)

    # Time: O(1) Space: O(1)
    def dequeue_any(self):
        return self.pop_head()

    # Time: O(n) Space: O(1)
    def dequeue_cat(self):
        current_node = self.startNode
        prev_node = None
        while current_node is not None:
            if isinstance(current_node.value, Cat):
                if prev_node is None:
                    self.startNode = current_node.next
                else:
                    prev_node.next = current_node.next
                self.size -= 1
                return current_node.value
            prev_node = current_node
            current_node = current_node.next
        return None

    # Time: O(n) Space: O(1)
    def dequeue_dog(self):
        current_node = self.startNode
        prev_node = None
        while current_node is not None:
            if isinstance(current_node.value, Dog):
                if prev_node is None:
                    self.startNode = current_node.next
                else:
                    prev_node.next = current_node.next
                self.size -= 1
                return current_node.value
            prev_node = current_node
            current_node = current_node.next
        return None