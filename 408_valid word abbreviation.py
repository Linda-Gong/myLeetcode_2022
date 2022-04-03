"""
408. Valid word abbreviation
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.
For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # two pointers
        # i-> word, j-> abbr
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == '0':
                    return False
                tmp = 0
                while j < len(abbr) and abbr[j].isdigit():
                    tmp = tmp*10 + int(abbr[j])
                    j += 1

                i += tmp

        return i==len(word) and j==len(abbr)


