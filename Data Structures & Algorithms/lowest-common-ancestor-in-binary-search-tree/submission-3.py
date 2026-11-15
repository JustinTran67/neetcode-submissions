# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # dfs using binary search properties. use cases to traverse tree: base case: out of range: return, one is less and one is greater than current node: return current node value, run into p or q: return the one you run into (p or q), both less than current: go left, both greater than current, go right. Work split in half each call, O(h) time -> (O(logn) for balanced tree and worst case O(n)). use global variable to sotre the final result
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

        # time complexity: O(h), space complexity O(h)
        # O(h) -> O(logn) for balanced tree and O(n) for degenerate tree
        