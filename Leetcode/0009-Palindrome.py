# Convert the integer to a string, reverse the string, and compare the reversed string to the original
# string.
# 
# # Python
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)
#         return s == s[::-1]
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rs = "".join(list(reversed(s)))
        if rs != s:
            return False
        return True
