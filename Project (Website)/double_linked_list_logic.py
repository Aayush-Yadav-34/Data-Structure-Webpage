# double_linked_list_logic.py

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete_at_beginning(self):
        if self.is_empty():
            return None
        deleted_node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return deleted_node.data

    def delete_at_end(self):
        if self.is_empty():
            return None
        if self.head.next is None:
            deleted_node = self.head
            self.head = None
            return deleted_node.data
        current = self.head
        while current.next:
            current = current.next
        deleted_node = current
        current.prev.next = None
        return deleted_node.data

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " <-> ".join(elements) + " <-> None"
