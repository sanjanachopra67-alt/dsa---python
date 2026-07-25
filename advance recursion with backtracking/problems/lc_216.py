"""Find all valid combinations of k numbers that sum up to n such that the 
following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the 
same combination twice, 
and the combinations may be returned in any order."""

class Solution(object):
    def solve(self, n, nums, last, total, k, res):
        if total == n and len(nums) == k:
            res.append(list(nums))
        if total > n or len(nums) > k:
            return
        for i in range(last,10):
            nums.append(i)
            self.solve(n, nums, i+1, total+i, k, res)
            nums.pop()
        

    def combinationSum3(self, k, n):

        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        nums = []
        self.solve(n, nums, 1, 0, k, res)
        return res