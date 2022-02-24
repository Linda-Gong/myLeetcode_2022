'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
class Solution:
    def lengthOfLongestSubstring(self, s:str) ->int:
        res = 0
        sub = ""

        for char in s:
            if char not in sub:
                sub = sub + char
                res = max(res, len(sub))
            else:
                index = sub.index(char)
                sub = sub[index + 1:] + char

        return res

    # slicing window
    def lengthOfLongestSubstring2(self, s):
        chars = [0]* 128
        left, right = 0, 0
        res = 0

        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right-left+1)

            right += 1

        return res

x = Solution()
print(x.lengthOfLongestSubstring("abcabcbb"))
print(x.lengthOfLongestSubstring2("abcabcbb"))