"""151. Reverse Words in a String
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces."""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr = ""
        res = []
        for ch in s:
            if ch != " ":
                curr += ch
            else: 
                if curr:
                    res.append(curr)
                    curr = ""
        if curr:
            res.append(curr)
        res = res[::-1]

        result = ""
        for i in range(len(res)):
            result += res[i]
            if i != len(res)-1:
                result += " "
        return result 
    


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        res = " ".join(words)
        return res