# 1. Create a list of strings with length equal to the number of rows. 
# 2. Create a variable called going_down that is True. 
# 3. Create a variable called count that is equal to the first row. 
# 4. Create a variable called rows that is equal to the number of rows minus 1. 
# 5. Iterate through the string. 
# 6. If going_down is True, add the letter to the string at the index count. 
# 7. Increment count by 1. 
# 8. If count is

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [""] * numRows
        rows = numRows -1 
        going_down = True
        count = 0
        for letter in s:
            if going_down: 
                res[count]+=letter
                count+=1 
            if not going_down:
                count -= 1
                res[count]+=letter
            if count <= 0:
                going_down = True 
                count += 1
            if count > rows: 
                going_down = False 
                count -= 1
        return ("".join(res))
