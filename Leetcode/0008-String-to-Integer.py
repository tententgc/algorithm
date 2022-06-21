# 1. Remove all the whitespaces in the string.
# 2. Find all the numbers in the string.
# 3. If the number is "-0", return 0.
# 4. If the number is greater than 2**31-1, return 2**31-1.
# 5. If the number is smaller than -2**31, return -2**31.
# 6. Return the number.
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        answer_lst = re.findall(r'^[-+]?[\d]+', s)

        if not answer_lst or answer_lst[0] == "-0":
            return 0

        answer = answer_lst[0]
        if int(answer_lst[0]) < -2**31:
            answer = -2**31
        if int(answer_lst[0]) > 2**31-1:
            answer = 2**31-1

        return int(answer)
