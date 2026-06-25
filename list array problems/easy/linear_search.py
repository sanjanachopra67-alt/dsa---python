""" Given an array arr[] of n integers and an integer x,
 return the index of the first occurrence of x,
 or -1 if not found.
"""
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1