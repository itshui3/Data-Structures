import sys

sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        # necessarily sets up with a value
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        pass

    def re_checkplace(self, node, value):
        pass

    def contains(self, target):
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass

    def in_order_print(self, node):
        pass

    def bft_print(self, node):
        pass

    def dft_print(self, node):
        pass

    def pre_order_dft(self, node):
        pass

    def post_order_dft(self, node):
        pass