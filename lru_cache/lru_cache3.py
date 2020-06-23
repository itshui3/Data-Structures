from doubly_linked_list import DoublyLinkedList

class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.current = 0
        self.dll = DoublyLinkedList()
        self.storage = {}

    def get(self, key):
        if key not in self.storage: return None
        self.dll.move_to_front(self.storage[key])
        return self.storage[key].value[1]

    def set(self, key, value):
        if key in self.storage:
            self.storage[key].value = [key, value]
        else:
            self.dll.add_to_head([key, value])
            self.storage[key] = self.dll.head
            self.current += 1
        
        if self.current > self.limit:
            key = self.dll.tail.value[0]
            del self.storage[key]
            self.dll.remove_from_tail()
            self.current -= 1