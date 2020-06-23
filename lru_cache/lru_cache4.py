from doubly_linked_list import DoublyLinkedList

class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.current = 0
        self.dll = DoublyLinkedList()
        self.storage = {}

    def set(self, key, value):
        if key not in self.storage:
            self.dll.add_to_head([key, value])
            self.storage[key] = self.dll.head
            self.current += 1
        else:
            self.storage[key].value = [key, value]
            self.dll.move_to_front(self.storage[key])

        if self.current > self.limit:
            tail_key = self.dll.tail.value[0]
            del self.storage[tail_key]
            self.dll.remove_from_tail()
            self.current -= 1
    
    def get(self, key):
        if key in self.storage:
            self.dll.move_to_front(self.storage[key])
            return self.storage[key].value[1]
        else:
            return None