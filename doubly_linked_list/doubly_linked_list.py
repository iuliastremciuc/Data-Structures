"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
      
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        
        # Create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1 

        # If DLL is empty
        if self.head is None:
            #set head and tail to the new node instence
            self.head = new_node   
            self.tail = new_node     
        
        # If DLL is not empty
        else:
            #set new node's next to current head
            new_node.next = self.head
            #set head's prev to the new node
            self.head.prev = new_node
            #set head to the new node
            self.head = new_node


        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    # def remove_from_head(self):
        
    #     # store the value of the head
    #     head_value = self.head
    #     # decrement the length of the DLL
    #     self.length -= 1        
    #     # delete the head
    #         # if head.next is not None
    #     if head_value.next != None:
    #             # set head.next's prev to None
    #         head_value.next.prev  = head_value.prev
    #            # else (if head.next is None)
    #     if head_value.next is None:
    #             # set head to None
    #         self.head = None
    #             # set tail to None
    #         self.tail = None

    #     return head_value.value
    
    
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
                
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        
        # Create instance of ListNode with value
        new_node = ListNode(value)
        # incrementthe DLL length attribute
        self.length += 1

        # If DLL is empty
        if self.head is None:
            #set head and tail to the new node instence
            self.head = new_node   
            self.tail = new_node 
           
        
        # If DLL is not empty
        else:
            #set new node's prev to current head
            new_node.prev = self.tail
            #set head's next to the new node
            self.tail.next = new_node
            #set head to the new node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    # def remove_from_tail(self):
        
    #     # store the value of the tail
    #     new_node = self.tail
    #     # decrement the length of the DLL
    #     self.length -= 1
    #     # delete the tail
    #         # if tail.prev is not None
    #     if new_node.prev != None:
    #             # set tail.prev's next to None
    #         new_node.prev.next = new_node.next
    
    #         # else (if tail.prev is None)
    #     if new_node.prev is None:

    #             # sed head to None
    #         self.head = None

    #             # set tail to None
    #         self.tail = None

    #     return new_node.value


    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        new_node = self.head
        place = None
        if not new_node or not new_node.next:
            return
        if new_node and new_node.next:
            place = new_node
            new_node = new_node.next

        place.next = None
        new_node.next = self.head
        self.head = new_node

    # def move_to_front(self, node):
    #     if node is self.head:
    #         return
    #     value = node.value
    #     if node is self.tail:
    #         self.remove_from_tail
    #     else:
    #         node.delete()
    #         self.length +=1
    #         self.add_to_head()


        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        new_node = self.tail
        place = None
        if not new_node or not new_node.prev:
            return
        if new_node and new_node.prev:
            place = new_node
            new_node = new_node.prev

        place.prev = None
        new_node.prev = self.tail
        self.tail = new_node


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        
        if not self.head:
            return
        
        self.length -= 1
        ## Dll is length of 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            
        elif self.tail == node:
            self.tail = node.prev
           
        else:
            node.delete()



    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = self.head.value
        temp = self.head
        while temp:
            if temp.value > max:
                max = temp.value
            temp = temp.next
        return max


dll = DoublyLinkedList()
# dll.add_to_head(2)
# dll.remove_from_head()  
print(dll)  