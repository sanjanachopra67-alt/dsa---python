# LeetCode 1021: Remove Outermost Parentheses
# Given a valid parentheses string s, remove the outermost parentheses of every primitive string.

class Solution:
    def removeOuterParentheses(self, s):
        res = []
        depth = 0

        for ch in s:
            if ch == '(':
                if depth > 0:
                    res.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res.append(ch)

        return "".join(res)