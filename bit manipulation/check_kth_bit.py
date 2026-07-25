class Solution:
    def checkKthBit(self, n, k):
        if n & (1 << k) != 0:
            return True
        return False