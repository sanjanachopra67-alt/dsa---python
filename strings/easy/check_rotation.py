"""The Rotate String problem asks us to check whether one string goal can be obtained by rotating another string s.

A rotation means repeatedly moving the leftmost character of a string to the rightmost position.
We need to return True if after some number of rotations, s can become goal; otherwise return False."""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        string = s + s
        return goal in string