from doubly_linked_list import DoublyLinkedList

class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

   
    def get(self, key): #O(1)
        if key in self.storage:
            node = self.storage[key]            
            self.order.move_to_end(node)
            return node.value[1]

        else: 
            return None

   
    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        if self.size == self.limit:
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()
            self.size -= 1

        self.size += 1
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
                     
        # create node if key not found and move to FRONT
        # move node to front if found
        # if full REMOVE LAST node from list and dictionary
     
