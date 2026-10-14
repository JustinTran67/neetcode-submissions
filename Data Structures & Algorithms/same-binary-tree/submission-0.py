# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is None):
            return True
        elif (p is None and q) or (p and q is None) or (p.val != q.val):
            return False
        match1 = self.isSameTree(p.left, q.left)
        match2 = self.isSameTree(p.right, q.right)
        if (not match1 or not match2):
            return False
        return True
        
        