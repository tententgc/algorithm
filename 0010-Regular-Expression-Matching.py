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
    def isMatch(self, s: str, p: str) -> bool:
        if re.compile('^'+p+'$').match(s):
            return True
        return False
