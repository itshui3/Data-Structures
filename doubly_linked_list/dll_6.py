class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node else 0
        self.max = node.value if node else None

    def __len__(self):
        return self.length

    def add_to_head(self, value):

    # create a new_node
        new_node = ListNode(value, None, None)
        self.length += 1
    # make old node next_node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    # make the new node head
    # if no old node new_node == head/tail
    # update length in all cases
 
    def remove_from_head(self):
        # cases:
        # 1] no nodes, just return
        # 2] one node, no sideways pointers. but both head and tail pointing to same node.
        # make them both None
        # more than one
        # 3] reassign head to inner node
        # 4] remove right pointers
        # 5] decrement length
        if self.head is None: return

        value = self.head.value
        self.length -= 1

        if self.head == self.tail:
            self.head, self.tail = None, None
            return value
        else: 
            node = self.head
            self.head = self.head.next
            self.head.prev = None
            node.next = None
            return value


    def add_to_tail(self, value):
        # 1.
        # create a new_node
        # 2. attach the node
        # a. since node is the last one, it has a prev, and the prev is the previous tail
        # b. since the previous tail is the previous last node. It didn't ahve a next pointer, but now it does
        # that next pointer points to the new_node
        # c. point the tail pointer to the new node
        # add 1 to length
        new_node = ListNode(value)
        self.length += 1

        if self.tail is None: 
            self.head, self.tail = new_node, new_node
            return
        
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        

    def remove_from_tail(self):
        if self.tail is None: return

        value = self.tail.value
        self.length -= 1

        if self.head == self.tail:
            self.head, self.tail = None, None
            return value
        else: 
            node = self.tail
            self.tail = self.tail.prev
            # self.tail.next = None
            # node.prev = None
            node = None
            return value

    def move_to_front(self, node):
        if self.length < 2: return

        if node == self.head: return

        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            node.prev = None

        else:
            node_prev = node.prev
            node_next = node.next

            node_prev.next = node.next
            node_next.prev = node.prev
            node.prev = None

        node.next = self.head
        self.head.prev = node

        self.head = node
        

    def move_to_end(self, node):
        if self.length < 2: return

        if node == self.tail: return

        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            node.next = None

        else:
            node_prev = node.prev
            node_next = node.next

            node_prev.next = node.next
            node_next.prev = node.prev
            node.next = None

        node.prev = self.tail
        self.tail.next = node

        self.tail = node

    def delete(self, node):
        pass

    def get_max(self):
        
        if self.length == 0: return None

        if self.length == 1: return self.head.value

        else:

            return self.re_get_max(self.head)

    def re_get_max(self, cur):
        next_val = None
        if cur.next is not None:
            next_val = self.re_get_max(cur.next)

        if next_val is None or cur.value > next_val:
            return cur.value
        else:
            return next_val