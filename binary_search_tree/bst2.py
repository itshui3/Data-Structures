import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

# U:
# if BST is initialized with a value, we can assume that root is not None
    def insert(self, value):
        if self.value is None:
            self.value = value
            return

        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
# U:
# if I treat target as a value I'm placing, where would it go?
    def contains(self, target):
        if self.value is None: return False
        
        if self.value == target: return True

        else:
            if target < self.value:
                if self.left is None: return False
                else:
                    return self.left.contains(target)
                
            else:
                if self.right is None: return False
                else:
                    return self.right.contains(target)

    def get_max(self):
        if self.value is None: return None
        
        if self.right is None: return self.value

        else:
            return self.right.get_max()

    def for_each(self, cb):
        if self.value is None: return None
        
        cb(self.value)

        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    def in_order_print(self, node=None):
        if self.left is not None:
            self.left.in_order_print()
        if self.value is not None:
            print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)

        while q.len() > 0:
            dq = q.dequeue()
            print(dq.value)
            if dq.left is not None:
                q.enqueue(dq.left)
            if dq.right is not None:
                q.enqueue(dq.right)

    def dft_print(self, node):
        s = Stack()
        s.push(node)

        while s.len() > 0:
            pop = s.pop()
            print(pop.value)
            if pop.right is not None:
                s.push(pop.right)

            if pop.left is not None:
                s.push(pop.left)

    def pre_order_dft(self, node=None):
        if self.value is not None:
            print(self.value)

        if self.left is not None:
            self.left.pre_order_dft()

        if self.right is not None:
            self.right.pre_order_dft()

    def post_order_dft(self, node=None):
        
        if self.left is not None:
            self.left.post_order_dft()

        if self.right is not None:
            self.right.post_order_dft()

        if self.value is not None:
            print(self.value)