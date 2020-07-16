"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue 
from stack import Stack   
    
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert here
            if self.left is None:
                self.left = BSTNode(value)
            # Else:
            else:
                # repeat the proces on left subtree
                self.left.insert(value)
            
        # Case 2: value is greater than self.value
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        # Case 3; if value has duplicates


            
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #Case 1: self.value is equal to the target
        if self.value == target:
            return True
        #Case 2 : target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        #Case 3:  otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        # pass

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        #### Example solution 1
        # if not self:
        #     return None
        # if not self.right:
        #     return self.value
        # return self.right.get_max()

        #### Example solution 2
        # max_value = self.value
        # current = self
        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        # return max_value
        
        while self.right:
            self = self.right            
        return self.value
        # pass

    # Call the function `fn` on the value of each node
    def for_each(self, cb):
        cb(self.value)
        if self.right: 
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
        # pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current node is none
        # we know we have reached the end of recursion
        # base case we want to return

        if self is None:
            return
        # check if we can "move left"
        if self.left:
            self.left.in_order_print(node)
        # visit the node by rinting its value
        print(self.value)
        # check if we can "move right"
        if self.right:
            self.right.in_order_print(node)

        
    

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # import the queus class from earlier in the week
        # and use that class to implement this method

        # Use a queue to form a "line"
        # for the nodes to "get in"
        queue = Queue()
        queue.enqueue(node)

        # start by placing the root in the queue

        # need a while loop to iterate
        while len(queue) > 0:
            q = queue.dequeue()
            print(q.value)
            

        # what are  we checking in the while statement?
        # while length of ques is greater than 0
            # dequeue item from front of queue
            # print that item

            # place current item's left node in queue
            if q.left:
                queue.enqueue(q.left)
            if q.right:
                queue .enqueue(q.right)
            # place current item's right node in queue



        # pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    
    def dft_print(self, node):
        # import the stack class from earlier in the week
        # and use that class to implement this method

        # initialize an empty stack 
        stack = Stack()
        stack.push(node)
        # push  the root node onto the stack

        # need a while looop to manage our iteration 
        # if stack is not empty enter the while loop
        while len(stack) > 0:
            # pop top item off the stack 
            s = stack.pop()
            # print that item's value
            print(s.value)

            # if there is a right subtree
            if s.right:
                stack.push(s.right)
                # push right item onto the stack

            # if there is a left subtree
            if s.left:
                stack.push(s.left)
                # push left item onto  the stack

        # pass
# 
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        #  #preorder
        if self is None:
            return
        # check if we can "move left"
        print(self.value)
        if self.left:
            self.left.pre_order_dft(node)
        
        # check if we can "move right"
        if self.right:
            self.right.pre_order_dft(node)
        # pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self is None:
            return
        # check if we can "move left"
        if self.left:
            self.left.post_order_dft(node)
        
        # check if we can "move right"
        if self.right:
            self.right.post_order_dft(node)
        print(self.value)
