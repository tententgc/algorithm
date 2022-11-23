class Solution:
    def reverseBits(self, n: int) -> int:
        return int((bin(n).replace("0b","").rjust(32,"0"))[::-1],2)