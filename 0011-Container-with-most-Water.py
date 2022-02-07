# Use the `re` module to compile a regular expression pattern object. 
# 
# Use the `match` method to match the regular expression pattern object with a string. 
# 
# Use the `^` and `$` to match the whole string. 
# 
# Use the `.` to match any character. 
# 
# Use the `*` to match 0 or more repetitions of the preceding regular expression. 
# 
# Use the `+` to match 1 or more repetitions of the preceding regular expression. 
# 
# Use the `?` to match

class Solution:
    def maxArea(self, height: List[int]) -> int:
        best_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if best_area < area:
                best_area = area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return best_area