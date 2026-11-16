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

        while q: # time: O(level) with each node per level work = O(n) traversal
            length = len(q)
            level = []
            
            for i in range(length):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level[-1])

        return res

        # time complexity: O(n), space: O(n)

