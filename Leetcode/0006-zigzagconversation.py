class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [""] * numRows
        rows = numRows - 1
        down = True
        count = 0
        for letter in s:
            if down:
                res[count] += letter
                count += 1
            if not down:
                count -= 1
                res[count] += letter
            if count <= 0:
                down = True
                count += 1
            if count > rows:
                down = False
                count -= 1
        return "".join(res)
