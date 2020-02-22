import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self, value):
        if self.size > 0:
            self.size -= 1
            self.storage.remove_from_head()
        else:
            return None
    def len(self, value):
        return self.size

# using list in terms of time complex,
# cost of adding/removing end of list: 
# O(1) array is directly space efficient, can fit double arrays
# for Queue, list vs arry is diff because we add TO/FROM back no matter what