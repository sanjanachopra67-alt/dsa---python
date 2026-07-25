class Solution:
    def reverse(self, head):
        # code here
        if not head or head.next:
            return head
        
        current = head
        new_head = None
        
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            new_head = current
            current = current.prev
        return new_head
                