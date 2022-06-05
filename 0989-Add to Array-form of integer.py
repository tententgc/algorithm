class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        nums = (int("".join(list(map(str, num))))) + k
        op = [int(i) for i in str(nums)]
        return op
