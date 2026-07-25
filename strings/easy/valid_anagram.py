"""The Valid Anagram problem asks us to check if two given strings s and t are anagrams of each other.

An anagram is a word or phrase formed by rearranging the letters of another word.
Both strings must use the same letters with the same frequency.
If they are anagrams, return True; otherwise, return False."""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for ch in s:
            chars[ch] = chars.get(ch, 0) + 1
        for ch in t:
            if ch not in chars:
                return False
            else:
                if chars[ch] == 0:
                    return False
                chars[ch] -= 1
        return True