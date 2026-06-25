"""
Given an array arr[].
The task is to find the largest element and return it.
"""
class Solution:
    def largest(self, arr):
        largest = arr[0]
        for i in range(0,len(arr)):
            largest = max(largest,arr[i])
        return largest
    