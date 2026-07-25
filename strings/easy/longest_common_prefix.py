"""The Longest Common Prefix problem asks us to find the longest string prefix that is common to all strings in a given list.

A prefix of a string is the beginning part of the string.
If there is no common prefix at all, return an empty string """""

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        result = ""
        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return result
            result += base[i]
        return result