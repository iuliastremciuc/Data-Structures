from singly_linked_list import Node, LinkedList
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = []
#         # self.storage = ?
#     def __str__(self):
#         return f"{self.size}"
    
#     def __len__(self):
#         return len(self.size)

#     def enqueue(self, value):
#         self.size.insert(0,value)

#     def dequeue(self):
#         if len(self.size) == 0:
#             pass
#         else:
#             v = self.size[len(self.size)-1]
#             self.size.pop()
#             return v

# q = Queue()
# q.enqueue(100)
# q.enqueue(101)
# q.enqueue(105)
# print(q)
# q.dequeue()
# print(q)


class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?
    
    def __len__(self):
        pass

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass