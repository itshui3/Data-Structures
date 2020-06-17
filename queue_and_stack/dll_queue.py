import sys
sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList

from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0: return None
        dequeue = self.storage[0]
        self.storage = self.storage[1:]
        self.size -= 1
        return dequeue

    def len(self):
        return self.size

class ListQueue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = LinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size = self.storage.length

        if self.size != self.storage.length:
            return 'Error, underlying structures unsynced'

    def dequeue(self):
        if self.size == 0: return None
        val = self.storage.remove_from_head()
        self.size = self.storage.length

        return val

    def len(self):
        # enqueue / dequeue logic must adjust size given operation successful
        if self.size != self.storage.length:
            return 'Error, underlying structures unsynced'
        else:
            return self.size