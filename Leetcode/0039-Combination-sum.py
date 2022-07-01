class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        for i in range(len(candidates)):
            if candidates[i] == target:
                combinations.append([candidates[i]])
            elif candidates[i] < target:
                rest = self.combinationSum(candidates[i:], target - candidates[i])
                combinations += [[candidates[i]] + x for x in rest]
        return combinations
