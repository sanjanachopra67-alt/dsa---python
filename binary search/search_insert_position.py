# LeetCode 35: Search Insert Position
# Given a sorted array of distinct integers and a target, return the index if found, else the index where it would be if inserted in order.

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left