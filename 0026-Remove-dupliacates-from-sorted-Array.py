class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      if len(nums) == 0:
          return 0
      insertIndex = 0
      for i in range(1, len(nums)):
        if nums[i] != nums[insertIndex]:
          nums[insertIndex+1] = nums[i]
          insertIndex += 1
      return insertIndex + 1
