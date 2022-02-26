"""
1405. Longest Happy String
A string s is called happy if it satisfies the following conditions:
s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.

"""
class Solution:
    def longestDiverseString(self, a:int, b:int, c:int) -> str:
        dic = {'a':a, 'b':b, 'c':c}
        res = []

        while True:
            pre = len(res)
            self.try_append(dic, res)
            after = len(res)
            if pre == after:
                break

        return "".join(res)

    def try_append(self, dic, res):
        tmp = [(val, key) for key, val in dic.items()]
        tmp.sort(reverse=True)
        first, second, third = tmp  # e.g first = (6, 'a')

        # not append first
        if len(res) >= 2 and res[-2] == res[-1] == first[1]:
            if second[0] > 0:
                res.append(second[1])
                dic[second[0]] -= 1
            else:
                return

        # append first
        else:
            if first[0] > 0:
                res.append(first[1])
                dic[first[0]] -= 1
            else:
                return




