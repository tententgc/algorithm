 def lengthOfLongestSubstring(self, s: str) -> int:
       if len(s) < 2:
            return len(s)

        substring = ""
        maxlength = 0

        for ch in s:
            if ch not in substring:
                substring += ch
                if len(substring) > maxlength:
                    maxlength = len(substring)

            else:
                while ch in substring:
                    substring = substring[1:]
                substring += ch

        return maxlength
print(lengthOfLongestSubstring("abcabcbb"))