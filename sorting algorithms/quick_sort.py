"""
Description:
Divide and conquer algorithm that selects a pivot and partitions the array.

Time Complexity:
Best: O(n log n)
Average: O(n log n)
Worst: O(n^2)

Space Complexity:
O(log n) (recursive stack)
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)