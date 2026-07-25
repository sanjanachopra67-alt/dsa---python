"""Given a string containing digits from 2-9 inclusive,
 return all possible letter combinations that the number could represent.
 Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
 Note that 1 does not map to any letters."""

class Solution(object):
    def __init__(self):
        self.phone_map = {
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
    def solve(self, index, digits, res, curr):
        if index == len(digits):
            res.append(curr)
            return
        options = self.phone_map.get(digits[index], "")

        for char in options:
            self.solve(index+1, digits, res, curr+char)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        self.solve(0, digits, res, "")
        return res