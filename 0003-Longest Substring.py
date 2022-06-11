class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        sub = ''
        for ch in s:
            if ch in s:
                sub = sub[sub.find(ch)+1:]
            sub += ch
            if len(sub) > max_l:
                max_l = len(sub)
        return max_l
