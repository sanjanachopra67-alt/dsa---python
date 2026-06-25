# Reverse an array using recursion

def reverse_array(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array(arr, left + 1, right - 1)