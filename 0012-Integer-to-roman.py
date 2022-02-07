# Find the maximum area of a rectangle formed by two pointers.
# 
# # <details>
# # <summary>
# # <font size="3" ><b>Detailed Explanation of the Code </b></font>
# # </summary>
# # 
# # 
# # * The code starts with the initialization of the variables `best_area` and `l` and `r` to 0. 
# # 
# # 
# # * The outer while loop is executed as long as the left pointer is less than the right pointer. 
# #
# A simple program that prints out the numbers from 1 to 100.
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for k in d:
            while num >= k:
                res += d[k]
                num -= k
        return res
