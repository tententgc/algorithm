class Solution:
    def divide(self, dividend: int, divisor: int):
        pos = 1 if (dividend > 0) == (divisor > 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if pos < 0:
            res = -res
        return min(max(-2147483648, res), 2147483647)
