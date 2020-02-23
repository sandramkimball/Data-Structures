import sys
sys.path.append('../queue_and_stack')
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
        if targt < self.value:
            if not self.left:
                return False
            else:
                self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                self.right.contains(target)

    # Return the maximum value in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    def for_each(self, cb):
        cb(self.value):
            if self.left:
                self.left.for_each(cb)
            if self.right:
                self.right.for_each(cb)

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
                print(f'{self.left.for_each()}')
        if self.right:
            print(f'{self.right.for_each()}')


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if self.left:
                print(f'{self.left.for_each()}')
        if self.right:
            print(f'{self.right.for_each()}')

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass






    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
