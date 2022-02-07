# For each element in the list, check if the target - element exists in the rest of the list. 
# 
# If it does, return the index of the element and the index of the target - element. 
# 
# If it doesn't, continue to the next element. 
# 
# If you've gone through all the elements and haven't found a match, return an empty list.
# 
# # Python
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
