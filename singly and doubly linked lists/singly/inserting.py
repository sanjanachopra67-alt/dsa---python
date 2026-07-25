class Node:
    def __init__(self, val=None):
        self.val = val          # Stores the value of this node
        self.next = None        # Points to the next node (initially None)

def insert_at(self, data, position):
    new_node = Node(data)
    if position == 0:
        new_node.next = self.head
        self.head = new_node
    else:
        current = self.head
        prev_node = None
        count = 0
        while current is not None and count < position:
            prev_node = current
            current = current.next
            count += 1
        new_node.next = current
        if prev_node:
            prev_node.next = new_node