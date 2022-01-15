class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rs = "".join(list(reversed(s)))
        if rs != s:
            return False
        return True
