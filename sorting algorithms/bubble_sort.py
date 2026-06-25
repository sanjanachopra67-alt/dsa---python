"""
Description:
Repeatedly compares adjacent elements and swaps them if they are in the wrong order.

Time Complexity:
Best: O(n)
Average: O(n^2)
Worst: O(n^2)

Space Complexity:
O(1) (in-place)
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr