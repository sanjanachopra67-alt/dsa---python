class Solution:
    def get(self, a, b):
        a = a ^ b  # Step 1: a now holds XOR of original a and b
        b = a ^ b  # Step 2: b now holds original a
        a = a ^ b  # Step 3: a now holds original b
        return [a, b]