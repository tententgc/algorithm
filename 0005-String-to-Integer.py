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
