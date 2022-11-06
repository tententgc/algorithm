class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return min(s[i:]+s[:i] for i in range(len(s))) if k==1 else "".join(sorted(s))