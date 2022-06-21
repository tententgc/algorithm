# 1. Sort the array. 
# 2. Loop through the array and find all the possible combinations of two numbers that add up to the
# target. 
# 3. For each combination, find the other two numbers that add up to the target. 
# 4. If the combination is found, add it to the solution.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() 
        
        solution = {}
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                start = j+1 
                end = len(nums)-1 
                
                while (start <  end):
                    temp = nums[i]+nums[j]+nums[start]+nums[end] 
                    
                    if (temp == target): 
                        solution[nums[i],nums[j],nums[start],nums[end]] = True
                        start += 1
                        end -= 1
                    elif temp < target:
                        start += 1 
                    else : 
                        end -= 1 
        return solution.keys()