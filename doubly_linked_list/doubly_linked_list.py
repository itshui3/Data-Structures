"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


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
        self.head, self.tail, self.length = node, node, 1 if node else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        self.length += 1
        # head & tail are both None, nothing in linked list
        new_node = ListNode(value)
        if self.head == None: self.head, self.tail = new_node, new_node
        else: self.head.prev, new_node.next, self.head = new_node, self.head, new_node
 
    def remove_from_head(self):
        if self.length < 1: return None

        self.length -= 1

        removed = self.head
        if self.head == self.tail: self.head, self.tail = None, None
        else: self.head, self.head.prev, removed.next = self.head.next, None, None
        
        return removed.value

    def add_to_tail(self, value):
        self.length += 1
        # head & tail are both None, nothing in linked list
        new_node = ListNode(value)
        if self.head is None: self.head, self.tail = new_node, new_node
        else: new_node.prev, self.tail.next, self.tail = self.tail, new_node, new_node

    def remove_from_tail(self):
        if self.length < 1: return None

        self.length -= 1
        removed = self.tail
        if self.tail == self.head: self.tail, self.head = None, None
        else: self.tail, removed.prev, self.tail.next = self.tail.prev, None, None
        
        return removed.value

    def move_to_front(self, node):

        if self.head == node: return
        elif self.tail == node:
            self.tail, node.prev, self.tail.next = self.tail.prev, None, None
            node.next, self.head.prev, self.head = self.head, node, node
        else:
            node_prev, node_next = node.prev, node.next
            node_prev.next, node_next.prev = node_next, node_prev
            node.next, self.head.prev, self.head = self.head, node, node

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass

    def get_max(self):
        pass
