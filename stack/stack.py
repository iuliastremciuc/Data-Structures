from singly_linked_list import Node, LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = []
#         # self.storage = ?
#     def __str__(self):
#         return f"{self.size}"

#     def __len__(self):
#         return len(self.size)

#     def push(self, value):
#         self.size.append(value)

#     def pop(self):
#         if len(self.size) == 0:
#             pass
#         else:
#             v = self.size[len(self.size) - 1]
#             self.size.pop()
#             return v


# s = Stack()
# print(s)
# s.push(100)
# s.push(101)
# s.push(105)
# print(s)
# s.pop()
# print(len(s))


class Stack:
    def __init__(self):
        self.size = LinkedList()
        # self.storage = ?

    def __len__(self):
        return len(self.head)


    def push(self, value):
        self.size.add_to_tail(value)
        

    def pop(self):
        return self.size.remove_tail()

s = Stack()
s.push(100)
s.push(101)
s.push(105)
print(s)
s.pop()
print(s)


