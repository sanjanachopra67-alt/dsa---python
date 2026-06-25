"""
Given two sorted arrays a[] and b[], 
where each array may contain duplicate elements ,
the task is to return the elements in the union of the 
two arrays in sorted order.
Union of two arrays can be defined as the set 
containing distinct common elements that are present 
in either of the arrays.
"""
class Solution:
    def findUnion(self, a, b):
        # code here 
        i = 0
        j = 0
        res=[]
        while i<len(a) and j<len(b):
            if a[i] <= b[j]:
                if len(res)==0 or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            else:
                if len(res)==0 or res[-1] != b[j]:
                    res.append(b[j])
                j += 1
        while i<len(a):
            if len(res)==0 or res[-1] != a[i]:
                res.append(a[i])
            i += 1
        while j<len(b):
            if len(res)==0 or res[-1] != b[j]:
                res.append(b[j])
            j += 1
        return res