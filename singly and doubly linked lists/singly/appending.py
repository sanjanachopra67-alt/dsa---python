class Node:
    def __init__(self, val=None):
        self.val = val          # Stores the value of this node
        self.next = None        # Points to the next node (initially None)
        
def append(self, data):
    new_node = Node(data)      # Create a new node with the given value
    if not self.head:          # If the list is empty, set head to new node
        self.head = new_node
    else:
        current = self.head
        while current.next is not None:   # Traverse to the last node
            current = current.next
        current.next = new_node           # Link the last node to the new node