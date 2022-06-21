class Solution:
    def permute(self, nums):
        if len(nums) == 1: 
            return [nums]
        result = []
        for i in range(len(nums)): 
            o = nums[:i] + nums[i+1:]
            op = self.permute(o)
            for p in op: 
                result.append([nums[i]] + p)
        return result