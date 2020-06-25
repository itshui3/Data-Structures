import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def insert(self, value):
        
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)

                if self.right is None:
                    # this means height needs a bubble-update
                    return True
                else:
                    return False
            else:
                bubble = self.left.insert(value)

                if bubble: self.height += 1
                return bubble
            
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)

                if self.left is None:
                    # 
                    return True
                else:
                    return False
            else:
                bubble = self.right.insert(value)

                if bubble: self.height += 1
                return bubble

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None: 
                return False
            else:
                bubble = self.left.contains(target)
                if bubble == True: print(self.height)
                return bubble
        else:
            if self.right is None: 
                return False
            else: 
                bubble = self.right.contains(target)
                if bubble == True: print(self.height)
                return bubble
    def get_max(self):
        pass
    def for_each(self, cb):
        pass
    def in_order_print(self, node=None):
        pass
    def bft_print(self, node):
        pass
    def dft_print(self, node):
        pass
    def pre_order_dft(self, node=None):
        pass
    def post_order_dft(self, node=None):
        pass

bst = BinarySearchTree(1)
bst.insert(2)
bst.insert(3)
bst.insert(7)
print(bst.contains(7))
print(bst.contains(8))