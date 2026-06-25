# LeetCode 2149: Rearrange Array Elements by Sign
# Given an array nums with equal number of positive and negative integers, rearrange them so positives and negatives alternate, starting with a positive.

class Solution:
    def rearrangeArray(self, nums):
        res = [0] * len(nums)
        p, n = 0, 1
        for x in nums:
            if x > 0:
                res[p] = x
                p += 2
            else:
                res[n] = x
                n += 2
        return res