"""Given a non-empty array of integers nums, 
every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 """
class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        ans = start ^ goal
        count = 0

        for i in range(0,32):
            if ans & (1 << i) != 0:
                count += 1
        return count