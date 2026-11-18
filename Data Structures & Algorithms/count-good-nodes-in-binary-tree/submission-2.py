# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # naive/brute force solution, compare every node with every other node in its path, O(n^2) solution
        # proposed solution: dfs down every path and maintain a max value along every path comparing that value to the new leaves we reach. Increment for every value greater than the greatest.

        def dfs(node, greatest):
            if not node:
                return 0
            if node.val >= greatest:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            return dfs(node.left, greatest) + dfs(node.right, greatest)
        
        return dfs(root, root.val)

        # O(n) time, O(n) space

        
