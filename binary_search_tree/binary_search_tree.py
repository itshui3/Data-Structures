import sys

sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        self.re_checkplace(self, value)
        # if smaller than value in current
        # scope, check left for None
        # if greater than value in current
        # scope, check right for None
        # if None, create BST and place there
        # else recurse comparison on branch
    def re_checkplace(self, node, value):
        # receives branch node I'mchecking
        # and value needing a placement
        # recurses if checked node is not None
        # on that Node
        # returns if node can be placed
        if value < node.value:
            # check left
            if node.left is None:
                node.left = BinarySearchTree(value)
                return
            else:
                # recurse on node.left
                self.re_checkplace(node.left, value)
        else:
            # check right
            if node.right is None:
                node.right = BinarySearchTree(value)
                return
            else:
                self.re_checkplace(node.right, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        return self.re_check(self, target)
        # recursively check node, comparing greater/less
        # and passing in left/right to recurse_check
    def re_check(self, node, target):
        # check node.value against target
        if node is None: return False
        elif node.value == target: return True
        elif target < node.value:
            return self.re_check(node.left, target)
        else:
            return self.re_check(node.right, target)

    # Return the maximum value found in the tree
    def get_max(self):
        return self.re_check_max(self)
    def re_check_max(self, node):

        if node.right is not None:
            return self.re_check_max(node.right)
        else:
            return node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        self.re_for_each(self, cb)
        return

    def re_for_each(self, node, cb):
        cb(node.value)

        if node.left is not None:
            self.re_for_each(node.left, cb)
        if node.right is not None:
            self.re_for_each(node.right, cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        # 1. recursive approach
        # immediate = []
        # immediate.append(node)

        # 2. iterative queue approach
        q = Queue()
        q.enqueue(node)

        while q.len() > 0:
            resolve_node = q.dequeue()
            print(resolve_node.value)
            if resolve_node.left is not None:
                q.enqueue(resolve_node.left)
            if resolve_node.right is not None:
                q.enqueue(resolve_node.right)

    def re_level_print(self, immediate=[]):
        if len(immediate) == 0: return
        new_immediate = []
        while len(immediate) > 0:
            cur = immediate.pop()
            print(cur.value)
            if cur.right is not None:
                new_immediate.append(cur.right)
            if cur.left is not None:
                new_immediate.append(cur.left)
        self.re_level_print(new_immediate)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # 1. recursive dft
        # print(node.value)

        # if node.left is not None:
        #     self.dft_print(node.left)
        # if node.right is not None:
        #     self.dft_print(node.right)

        # 2. iterative stack approach
        s = Stack()
        s.push(node)

        while s.len() > 0:
            cur = s.pop()
            print(cur.value)

            if cur.right is not None:
                s.push(cur.right)
            if cur.left is not None:
                s.push(cur.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        
        print(node.value)
        if node.left is not None:
            self.pre_order_dft(node.left)
        if node.right is not None:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # lrp
        # check left node
        # if exist, recurse passing in node.left
        # if not exist, check right node
        # if exist, 
        if node.left is not None:
            self.post_order_dft(node.left)
        if node.right is not None:
            self.post_order_dft(node.right)
        print(node.value)


bst = BinarySearchTree(5)