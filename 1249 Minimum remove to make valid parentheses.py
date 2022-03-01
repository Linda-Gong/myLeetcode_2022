'''
Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = []
        stack = []
        for i in range(len(s)):
            if s[i] not in "()":
                continue
            if s[i] == "(":
                stack.append(i)
            elif not stack:
                index_to_remove.append(i)
            else: ## before pop check if empty or not. That's why the elif statement
                stack.pop()

        remove = index_to_remove + stack
        res = ""
        for i in range(len(s)):
            if i not in remove:
                res += s[i]

        return res
