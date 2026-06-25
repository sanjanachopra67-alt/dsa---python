# LeetCode 34: Find First and Last Position of Element in Sorted Array
# Given a sorted array nums and a target value, return the starting and ending position of target.

class Solution:
    def searchRange(self, nums, target):
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        return [find_first(nums, target), find_last(nums, target)]