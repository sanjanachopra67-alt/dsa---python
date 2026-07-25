class Node:
    def __init__(self, val=None):
        self.val = val          # Stores the value of this node
        self.next = None        # Points to the next node (initially None)
        
def traverse(self):
    if not self.head:
        print("Singly Linked List is empty")
    else:
        current = self.head
        while current is not None:
                print(current.val, end=" ")
                current = current.next
        print()