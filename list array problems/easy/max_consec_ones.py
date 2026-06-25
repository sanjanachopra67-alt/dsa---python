# LeetCode 485: Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count