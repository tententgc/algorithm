# 1. We start with an empty string, `outString`, and a string, `s`, that we want to find the longest
# palindrome in.
# 2. We start with a string, `outString`, that is the length of the longest palindrome we've found so
# far.
# 3. We iterate through the string, `s`, and for each character, `ch`, we add it to the end of the
# string, `temp`, and check if `temp` is a palindrome.
# 4. If `temp` is a pal

class Solution:
    def longestPalindrome(self, s: str) -> str:
        outString = ""
        while len(s) > len(outString):
            indLen = len(outString)
            temp = s[: indLen]
            for ch in s[indLen:]:
                temp += ch
                if temp == temp[::-1]:
                    outString = temp if len(temp) > len(
                        outString) else outString
            s = s[1:]
        return outString
