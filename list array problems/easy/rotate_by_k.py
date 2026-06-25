"""You have been given an array 'a' of 'n' integers and a number 'k'.
Rotate the array to the right by 'k' positions.
Return the rotated array.
"""
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)