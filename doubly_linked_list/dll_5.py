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
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)

        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            new_node.next, self.head.prev = self.head, new_node
            self.head = new_node
        
        self.length += 1

    def remove_from_head(self):

        if self.length == 0: return None
        node = self.head

        if self.length == 1:
            self.head, self.tail = None, None

        else:
            self.head = self.head.next
            node.next, self.head.prev = None, None
        
        self.length -= 1
        return node.value


    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0: 
            self.head, self.tail = new_node, new_node
        else:
            self.tail.next, new_node.prev = new_node, self.tail
            self.tail = new_node
        self.length += 1

    def remove_from_tail(self):
        if self.length == 0: return None
        node = self.tail

        if self.length == 1:
            self.head, self.tail = None, None
        else:
            self.tail = self.tail.prev
            self.tail.next, node.prev = None, None
        
        self.length -= 1
        return node.value

    def move_to_front(self, node):
        if node == self.head: return

        elif node == self.tail:
            self.tail = node.prev
            self.tail.next, node.prev = None, None
        
        else:
            node_prev, node_next = node.prev, node.next
            node_prev.next, node_next.prev = node.next, node.prev

        node.next, self.head.prev = self.head, node
        self.head = self.head.prev

    def move_to_end(self, node):
        if node == self.tail: return

        elif node == self.head:
            self.head = self.head.next
            node.next, self.head.prev = None, None

        else:
            node_prev, node_next = node.prev, node.next
            node_prev.next, node_next.prev = node.next, node.prev
        
        self.tail.next, node.prev = node, self.tail
        self.tail = node

    def delete(self, node):
        if self.length == 0: return

        if self.length == 1: self.head, self.tail = None, None

        elif node == self.head: 
            self.head = self.head.next
            node.next, self.head.prev = None, None

        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next, node.prev = None, None
        
        else:
            node_prev, node_next = node.prev, node.next
            node_prev.next, node_next.prev = node.next, node.prev
        
        self.length -= 1

    def get_max(self):
        return check_nvs(self.head)

def check_nvs(node):
    node_v = node.value
    print(node_v)

    if node.next is not None:
        nvs = check_nvs(node.next)

        if node_v > nvs: return node_v
        else: return nvs
    else:
        return node_v