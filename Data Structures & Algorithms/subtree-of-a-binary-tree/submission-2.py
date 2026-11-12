# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, p, q): # O(m) m = # of nodes in subroot, dfs checks like isSameTree
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)
            else:
                return False
   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        # main dfs runs in O(n) n = # of nodes in root and multiply by dfs time to get
        # O(n) * O(m) = O(n * m), space = O(hr) hr = height of root + O(hsr) hsr = height of subroot = O(n + m)