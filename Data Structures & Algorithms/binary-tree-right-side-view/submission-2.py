# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque # O(1) popping from left for queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs appraoch -> define a res array and define an internal dfs function that takes params node and depth, search right then left and if the depth equals the size of the res array, then that is the first (rightmost) node to append to res.

        res = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res

        # O(n), O(h) -> O(logn) or O(n) space
