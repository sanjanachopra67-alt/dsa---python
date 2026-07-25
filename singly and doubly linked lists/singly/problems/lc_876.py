"""876. Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node."""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n=0
        temp = head
        while temp is not None:
            n+=1
            temp = temp.next
        
        temp = head
        for i in range(0,n//2):
            temp = temp.next
        
        return temp
    
    # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tempslow = head
        tempfast = head

        while tempfast is not None and tempfast.next is not None:
            tempslow = tempslow.next
            tempfast = tempfast.next.next

        return tempslow