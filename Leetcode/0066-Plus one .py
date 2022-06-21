class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(list(map(str, digits))))
        num += 1
        q = [int(i) for i in str(num)]
        return q
