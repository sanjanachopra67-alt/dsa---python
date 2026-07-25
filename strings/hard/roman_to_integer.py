"""The Roman to Integer problem asks us to convert a given Roman numeral string into its corresponding integer value.

Roman numerals are represented using seven symbols:
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
Numbers are formed by combining these symbols and adding their values.
However, when a smaller value comes before a larger value, it is subtracted instead of added."""

class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping Roman numerals to their values
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If current value is less than the next one, subtract it
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        
        return total