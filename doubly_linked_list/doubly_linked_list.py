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
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:

            self.head.prev = new_node
            self.head = new_node
        self.length += 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):

        cur = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return cur.value
        else:
            self.head = cur.next
            cur.next = None
            self.head.prev = None
            self.length -= 1
            return cur.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, self.tail, None)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):

        if self.tail == self.head:
            cur = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return cur.value
        else:
            cur = self.tail
            self.tail = cur.prev

            cur.prev = None
            self.tail.next = None
            self.length -= 1
            return cur.value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):

        node_next = node.next
        node_prev = node.prev

        if node_prev is not None: node_prev.next = node_next
        if node_next is not None: node_next.prev = node_prev

        cur_head = self.head
        self.head = node

        cur_head.prev = node
        node.next = cur_head

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):

        cur = node

        if self.tail == node:
            return
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
            cur.next = None

            self.tail.next = cur
            cur.prev = self.tail
            self.tail = cur
        elif cur != self.head and cur!= self.tail:
            prev_node, next_node = cur.prev, cur.next
            prev_node.next, next_node.prev = next_node, prev_node

            self.tail.next = cur
            cur.prev = self.tail
            self.tail = cur
            


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        node_prev, node_next = node.prev, node.next

        if node_prev is not None:
            if node_next is not None:
                node_prev.next = node_next
                node_next.prev = node_prev
            else:
                node_prev.next = None
                self.tail = node_prev
        elif node_next is not None:
            node_next.prev = None
            self.head = node_next
        else:
            node = None
            self.head = None
            self.tail = None

        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        max_val = self.head.value
        cur_node = self.head
        while cur_node is not None:

            if cur_node.value > max_val:
                max_val = cur_node.value
            cur_node = cur_node.next
        return max_val
