class Node:
    def __init__(self, val=None):
        self.val = val          # Stores the value of this node
        self.next = None        # Points to the next node (initially None)

    def delete_head(self):
        if not self.head:
            print("Cannot delete. Singly Linked List is already empty")
        else:
            self.head = self.head.next  # The second node (or None) becomes the new head
    
    def delete(self, val):
        temp = self.head
        if temp and temp.val == val:
            self.head = temp.next
            return

        prev = None
        found = False

        while temp is not None:
            if temp.val == val:
                found = True
                break
            prev = temp
            temp = temp.next

        if found:
            prev.next = temp.next
        else:
            print("Node not found")