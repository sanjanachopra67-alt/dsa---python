"""Given the head of a sorted doubly linked list, remove all duplicate nodes from the list.
 Each node should appear only once in the final list."""

class Node:
    def __init__(self, value):
        self.data = value  # value stored in node
        self.next = None
        self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        # code here
        temp = headRef 
        nextnode = temp.next
       
        while temp:
            if temp.prev and temp.prev.data == temp.data:
                if temp.prev == headRef:
                    temp.prev = None
                    headRef = temp
                else:
                    temp.prev.prev.next = temp
                    temp.prev = temp.prev.prev
            temp = temp.next
        return headRef
                   