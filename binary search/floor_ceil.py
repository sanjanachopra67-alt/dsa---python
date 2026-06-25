# Given a sorted array arr and a number x, find the floor and ceil of x.
# Floor: greatest element <= x
# Ceil: smallest element >= x

def floor_ceil(arr, x):
    left, right = 0, len(arr) - 1
    floor_val, ceil_val = -1, -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return arr[mid], arr[mid]
        elif arr[mid] < x:
            floor_val = arr[mid]
            left = mid + 1
        else:
            ceil_val = arr[mid]
            right = mid - 1

    return floor_val, ceil_val