import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else: 
            return None

    def len(self):
        return self.size
