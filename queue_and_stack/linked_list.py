class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        pass

    def add_to_tail(self, value):
        # First In
        node = Node(value)

        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1


    def remove_from_head(self):
        # First Out
        if self.length == 0:
            return None

        if self.head == self.tail:
            removed = self.head
            val = removed.value
            self.head = None
            self.tail = None

            self.length -= 1
            return val
        else:
            removed = self.head
            val = removed.value

            self.head = self.head.next

            self.length -= 1
            return val

    def remove_from_tail(self):
        # Last Out
        # top of the stack
        if self.length == 0: return None

        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1

            return value
        else:
            val = self.tail.value

            cur = self.head
            while cur.next is not self.tail:
                cur = cur.next

            self.tail = cur
            cur.next = None
            self.length -= 1
            return val

# class Node:
#     def __init__(self, value=None, next_node=None):
#         self.value = value
#         self.next_node = next_node

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def add_to_head(self, value):
#         # create a node to add
#         new_node = Node(value)
#         # check if list is empty
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # new_node should point to current head
#             new_node.next_node = self.head
#             # move head to new node
#             self.head = new_node

#     def add_to_tail(self, value):
#         # create a node to add
#         new_node = Node(value)
#         # check if list is empty
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next_node = new_node
#             self.tail = new_node

#     def remove_head(self):
#         if not self.head:
#             return None
#         elif self.head == self.tail:
#             head_value = self.head.value
#             self.head = None
#             self.tail = None
#             return head_value
#         # otehrwise we have more than 1 value
#         head_value = self.head.value
#         self.head = self.head.next_node
#         return head_value

#     def contains(self, value):
#         if self.head is None:
#             return False

#         current_node = self.head

#         while current_node is not None:
#             if current_node.value == value:
#                 return True

#             current_node = current_node.next_node

#         return False

# linked_list = LinkedList()

# linked_list.add_to_head(0)
# linked_list.add_to_tail(1)
# print(f'does our LL contain 0? {linked_list.contains(0)}')
# print(f'does our LL contain 1? {linked_list.contains(1)}')
# print(f'does our LL contain 2? {linked_list.contains(2)}')

# linked_list.add_to_head(2)
# print(f'the start of the list is {linked_list.head.value}')