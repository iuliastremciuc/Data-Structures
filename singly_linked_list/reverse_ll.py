def reverse_ll(ll):
    """Receive a LinkedList as an input and return a reversed order LL
    
    Steps:
    1. Each node needs to point at the prev_node
    2. Head and tail pointers need to be flipped

    Cases:
    1. If the ll is empty return the otiginal that is passed in

    reverse_ll()
    """
    # # If LL is empty, return LL
    # if ll.head is None:
    #     return ll

    # # If LL has one node
    # if ll.head is ll.tail:
    #     return ll

    # If LL has more than one node
    current = ll.head
    previous = None
    next_node = None
    while current is not None:
        # store a poiner to the current next value
        next_node = current.get_next()

        # switch current's next pointer to the previous
        current.set_next(previous)
        
        # increment logic
        previous = current
        current = next_node
    
    ll.head, ll.tail = ll.tail, ll.head
         
        




