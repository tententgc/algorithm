class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]

        left = right = nums.index(target)

        while right+1 < len(nums) and nums[right+1] == target:
            right += 1

        return [left, right]
