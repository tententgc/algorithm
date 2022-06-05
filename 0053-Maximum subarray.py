class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        newnum = maxtotal = nums[0]
        for i in range(1, len(nums)):
            newnum = max(nums[i], nums[i] + newnum)
            maxtotal = max(maxtotal, newnum)
        return maxtotal
