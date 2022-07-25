class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""

        def solve(s, start, end):
            while (start >= 0 and end < len(s) and s[start] == s[end]):
                start -= 1
                end += 1
            return s[start+1:end]

        for i in range(len(s)):

            s1 = solve(s, i, i)
            s2 = solve(s, i, i+1)

            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2

        return res
