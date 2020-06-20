class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node else 0
        
    def __len__(self):
        # should return the length
        return self.length
    
    def add_to_head(self, value):
        # adds a new node to the front of the DLL
        new_node = ListNode(value)

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node

            self.head = new_node
        else:
            self.head, self.tail = new_node, new_node

        self.length += 1

    def remove_from_head(self):
        # removes head node and return it's value
        if self.length == 0: return None

        remove = self.head
        self.length -= 1
        if self.head == self.tail: 
            self.head, self.tail = None, None
            return remove.value

        else:
            self.head = self.head.next
            remove.next, self.head.prev = None, None

            return remove.value

    def add_to_tail(self, value):
        # adds a new node to the back of the DLL
        new_node = ListNode(value)
        self.length += 1
        if self.tail is None: self.head, self.tail = new_node, new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail

            self.tail = new_node

    def remove_from_tail(self):
        # removes tail node and returns it's value
        if self.length == 0: return None

        self.length -= 1

        removed = self.tail
        if self.head == self.tail:
            self.head, self.tail = None, None
            return removed.value

        else:
            self.tail = self.tail.prev
            self.tail.next, removed.prev = None, None

            return removed.value

    def move_to_front(self, node):
        # takes a node and moves it to the front
        if node == self.head: return

        if node == self.tail:
            self.tail = node.prev

            self.tail.next = None
            node.prev = None

            node.next = self.head
            self.head.prev = node

            self.head = node
        
        else:
            node_prev, node_next = node.prev, node.next
            node_prev.next, node_next.prev = node_next, node_prev

            node.next = self.head
            self.head.prev = node
            self.head = node

    def move_to_end(self, node):
        # takes a node and moves it to the end
        if node == self.tail: return

        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
        else:
            node_prev, node_next = node.prev, node.next
            node_prev.next, node_next.prev = node.next, node.prev

        node.prev = self.tail
        self.tail.next = node
        self.tail = node

        

    def delete(self, node):
        # deletes a node
        if self.length == 0: return None

        self.length -= 1
        if self.head == self.tail:
            self.head, self.tail = None, None

            return node.value
        
        elif node == self.head:
            self.head = self.head.next
            node.next, self.head.prev = None, None

            return node.value

        elif node == self.tail:
            self.tail = self.tail.prev
            node.prev, self.tail.next = None, None

            return node.value

        else:
            node_prev, node_next = node.prev, node.next
            node_prev.next, node_next.prev = node.next, node.prev

            return node.value

    def get_max(self):
        # gets the max value from the nodes and returns it
        return check_node(self.head)

def check_node(node):

    recurse_max = None
    if node.next is not None: recurse_max = check_node(node.next)

    if recurse_max is None:
        return node.value
    if node.value > recurse_max: 
        return node.value
    else:
        return recurse_max