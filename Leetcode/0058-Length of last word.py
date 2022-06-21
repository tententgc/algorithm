class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        q = s.split()
        g = len(q[-1])
        return g
