# LeetCode 53: Maximum Subarray
# Given an integer array nums, find the contiguous subarray with the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums):
        curr = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)
        return best