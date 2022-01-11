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
