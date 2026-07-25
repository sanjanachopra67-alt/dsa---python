"""Given a sorted doubly linked list of positive distinct elements, 
the task is to find pairs in a doubly-linked list whose sum is equal to given value target.
 """

from typing import Optional


from typing import List




class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None
"""
You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        left = head 
        right = head
        ans = []
        while right.next:
            right = right.next 
        while left is not None and right is not None and left != right and left.prev != right:
            if left.data + right.data == target:
                ans.append([left.data, right.data])
                left = left.next     
                right = right.prev
            elif left.data + right.data > target:
                right = right.prev
            else:
                left = left.next
        return ans
