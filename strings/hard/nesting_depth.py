"""The Maximum Nesting Depth of the Parentheses problem asks us to determine the deepest level of nested parentheses in a valid parentheses string.

You are given a string s consisting of digits and parentheses.
The nesting depth is the maximum number of open parentheses before they get closed.
Return the maximum depth of valid parentheses."""

class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr_depth = 0
        for brac in s:
            if brac == "(":
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif brac == ")":
                curr_depth -= 1
        return max_depth