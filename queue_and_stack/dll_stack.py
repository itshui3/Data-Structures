import sys
sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList

from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = []

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if self.size == 0: return None

        self.size -= 1
        return self.storage.pop()

    def len(self):
        return self.size

class ListStack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = self.storage.length

    def pop(self):
        if self.size == 0: return None
        val = self.storage.remove_from_tail()
        self.size = self.storage.length
        return val

    def len(self):
        if self.size != self.storage.length:
            return 'Underlying structure desync'
        return self.size