class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return true
        def dfs(l,r): 
            if not l and not r: 
                return True
            
            if not l or not r: 
                return False
            
            if l.val == r.val: 
                return dfs(l.left,r.right) and dfs(l.right,r.left)
            
            return False
        
        return dfs(root.left,root.right)
        