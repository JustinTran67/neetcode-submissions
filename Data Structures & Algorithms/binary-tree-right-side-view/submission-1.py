# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque # O(1) popping from left for queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # proposed solution: bfs on each level and only append the rightmost node.val that node being the one visible on the right. When we go through each level, the rightmost is always the last element at the level.
        if not root:
            return []
        
        res = [] # space: O(level) -> one element (rightmost) per level
        q = deque([root]) # space: O(n) -> can store at most all nodes

        while q:
            length = len(q)

            for i in range(len(q)):
                node = q.popleft()
                if i == length - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return res

        # time complexity: O(n), space: O(n)

