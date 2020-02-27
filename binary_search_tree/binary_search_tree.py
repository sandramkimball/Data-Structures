import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert a value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)

    # Return True if the tree contains the value
    def contains(self, target):
        if target == self.value:
           return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
               return False

    # Return the maximum value in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    def for_each(self, cb):
        if self.value:
            cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # Print all the values in order from low to high (Use recursive DFT)
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)


    # Print the value of every node:

    #BREADTH = QUEUE - WAIT IN LINE
    # 6 DEGREES OF BACON!!!
    #CHECK IF PATH EXISTS BETWEEN NODES, LAYER BY LAYER, DISTANCE AWAY
    def bft_print(self, node):
        #node(value, prev, next)
        #Queue (size, storage, head, tail)
        # edges = []... same as node.next, node.prev?
        # visited = false
        # parent = null
        storage = Queue()
        storage.enqueue(node)
        # visited = []

        while storage.len():
            current = storage.dequeue()
            print(current.value)

            if current.left:
                storage.enqueue(current.left)
                # visited.append(current.left)

            if current.right:
                storage.enqueue(current.right)
                # visited.append(current.right)
            
            # bft_print(self, current)


        
    #DEPTH = STACK - FIRST IN, FIRST OUT
    #BACKTRACKING, COMPLETE SEARCH, EXHAUSTS ALL POSS. PATHS
    def dft_print(self, node):
        storage = Stack()
        storage.push(node)

        while storage.len():
            current = storage.pop()
            print(current.value)

            if current.left:
                storage.push(current.left)
                # print(self.left)
                # self.left.bft_print(self.left)

            if current.right:
                storage.push(current.right)
                # print(self.right)
                # self.right.bft_print(self.right)

        # dft_print(self, current)





    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
