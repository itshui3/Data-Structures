from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.max = limit
        self.cur = 0
        # if cur == max, adding should remove LRU
        self.storage = DoublyLinkedList()
        # self.storage.head
        # self.storage.tail
        # self.storage.length
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.cache:
            self.storage.move_to_front(self.cache[key])
            return self.cache[key].value
        else: return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        if key not in self.cache: 
            self.cur += 1
            self.storage.add_to_head(value)
            self.cache[key] = self.storage.head
        else:
            print(self.cache[key].prev, self.cache[key].next)
            self.storage.move_to_front(self.cache[key])
            self.storage.head.value = value

        if self.cur > self.max: 
            self.storage.remove_from_tail()
            self.cur -= 1