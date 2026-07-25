"""Given head, the head of a linked list, determine if the linked list has a cycle in it. 
There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. 
Return true if there is a cycle in the linked list, 
otherwise return false."""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False 