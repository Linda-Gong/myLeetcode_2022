"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_str = min(strs)
        max_str = max(strs)
        for i in range(min(len(min_str), len(max_str))):
            if min_str[i] != max_str[i]:
                return min_str[:i]

        return min_str




