# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # dfs using binary search properties. use cases to traverse tree: base case: out of range: return, one is less and one is greater than current node: return current node value, run into p or q: return the one you run into (p or q), both less than current: go left, both greater than current, go right. Work split in half each call, O(h) time -> (O(logn) for balanced tree and worst case O(n)). use global variable to sotre the final result

        res = root

        def dfs(node):
            nonlocal res
            if not node:
                return
            if (p.val < node.val < q.val) or (q.val < node.val < p.val):
                res = node
                return
            if node.val == p.val or node.val == q.val:
                res = node
                return
            if p.val < node.val and q.val < node.val:
                dfs(node.left)
            if p.val > node.val and q.val > node.val:
                dfs(node.right)
        
        dfs(root)
        return res
            
        