class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.compile('^'+p+'$').match(s):
            return True
        return False