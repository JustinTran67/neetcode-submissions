# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # trivial solution -> place all elements vis dfs/bfs traversal into a BST into a list, sort the list, and then return the k-1 index approx. O(n) + O(nlogn) = O(nlogn) solution
        # proposed solution: in order traversal over BST and take advantage of the structure left < curr < right to sort elements into array and then return index k - 1 (1 indexed) full traversal = O(n) time and O(h) space depending on tree structure

        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            return
        
        dfs(root)
        return res[k - 1]


        