"""
Description:
Builds sorted array one element at a time by inserting elements in correct position.

Time Complexity:
Best: O(n)
Average: O(n^2)
Worst: O(n^2)

Space Complexity:
O(1) (in-place)
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr