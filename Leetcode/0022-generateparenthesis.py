class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[]
        res = []
        
        def solve(openp , closep): 
            if openp == closep == n: 
                res.append("".join(stack))
                return
            
            if openp < n: 
                stack.append("(")
                solve(openp + 1, closep)
                stack.pop()
                
            if closep < openp: 
                stack.append(")")
                solve(openp, closep+1)
                stack.pop()
                
        solve(0,0)
        return res