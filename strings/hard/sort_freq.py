"""The Sort Characters By Frequency problem asks us to rearrange the characters of a given string in descending order of frequency.

If multiple characters have the same frequency, their order does not matter.
The output should be a new string where characters appear grouped by frequency."""

class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        hash_map = {}
        
        # Step 1: Count frequencies
        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1

        # Step 2: Sort by frequency in descending order
        for ch, freq in sorted(hash_map.items(), key=lambda x: x[1], reverse=True):
            result += ch * freq  # Step 3: Build result string
        
        return result