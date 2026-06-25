class Solution(object):
    def countOccurrences(self, arr, target):
        
        def firstOccurrence():
            low, high = 0, len(arr) - 1
            first = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if arr[mid] == target:
                    first = mid
                    high = mid - 1   # move left
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return first
        
        def lastOccurrence():
            low, high = 0, len(arr) - 1
            last = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if arr[mid] == target:
                    last = mid
                    low = mid + 1   # move right
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return last
        
        first = firstOccurrence()
        
        if first == -1:
            return 0
        
        last = lastOccurrence()
        
        return last - first + 1