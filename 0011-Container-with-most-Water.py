class Solution:
    def maxArea(self, height: List[int]) -> int:
        best_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if best_area < area:
                best_area = area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return best_area