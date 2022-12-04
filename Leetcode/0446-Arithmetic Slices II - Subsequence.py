class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        freq = [defaultdict(int) for _ in range(len(nums))] #arthemetics subsequence
        for i,n in enumerate(nums): 
            for m in range(i): 
                diff = n - nums[m]
                res += freq[m].get(diff,0)
                freq[i][diff] += 1+ freq[m][diff]
        return res