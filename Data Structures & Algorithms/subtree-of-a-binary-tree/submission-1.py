# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(p, q): # O(m) m = # of nodes in subroot, dfs checks like isSameTree
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            else:
                return False

        if root.val == subRoot.val:
            res = dfs(root, subRoot)
            if res:
                return res
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)