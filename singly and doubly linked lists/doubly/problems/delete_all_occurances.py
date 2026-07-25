"""You are given the head of a doubly Linked List and a key x . 
Your task is to delete all occurrences of the given key x if it is present and return the new DLL.
"""
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
class Solution:
    
    # Function to delete all occurrences of x
    def deleteAllOccurOfX(self, head, x):
        # code here
        if not head.next and head.data == x:
            return None
        
        temp = head          # Pointer to traverse the list
        previous = None      # Pointer to track previous node
        new_head = head      # Keep track of new head
        
        # Traverse through the entire list
        while temp is not None:
            if temp.data == x:  # Found a node to delete
                # Update previous node's next pointer
                if previous:
                    previous.next = temp.next
                
                # Update next node's prev pointer
                if temp.next:
                    temp.next.prev = previous
                
                # Update head if we're deleting the first node
                if temp == new_head:
                    new_head = new_head.next
            
            previous = temp      # Move previous pointer
            temp = temp.next     # Move to next node
        
        return new_head