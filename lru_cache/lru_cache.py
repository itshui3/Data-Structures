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
        # there are cases where the keys still exist
        # but have been deleted off the DLL
        # this vvv if statement thinks the node still exists
        # so when move_to_front assumes that the node it's being
        # passed exists, it tries to move a node taht doesn't exist
        # to the front
        if key in self.cache:
            self.storage.move_to_front(self.cache[key])
            return self.cache[key].value[1]
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
        if key in self.cache:
            self.cache[key].value = [key, value]
            self.storage.move_to_front(self.cache[key])
        else:
            self.storage.add_to_head([key, value])
            self.cache[key] = self.storage.head
            self.cur += 1

        if self.cur > self.max: 
            # if I can delete the least recently used ref 
            # in cache by value-search rather than key lookup
            # I wouldn't have to use Tuples
            del self.cache[self.storage.tail.value[0]]
            self.storage.remove_from_tail()
            self.cur -= 1