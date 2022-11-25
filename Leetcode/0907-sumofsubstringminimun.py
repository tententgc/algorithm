class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        M = 10 ** 9 + 7 ;
        res  = 0 
        stack = []
        n = len(arr)
        arr.append(0)

        for i,num in enumerate(arr): 
            while stack and (i==0 or num < arr[stack[-1]]): 
                top = stack.pop()
                start = top - stack[-1] if stack else top +1
                ends = i - top 
                res += start * ends * arr[top]
                res %= M 

            stack.append(i)
        return res