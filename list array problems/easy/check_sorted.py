"""
Given an array arr[], check whether it is sorted in 
non-decreasing order. Return true if it is sorted otherwise 
false.
"""
class Solution:
    def isSorted(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True