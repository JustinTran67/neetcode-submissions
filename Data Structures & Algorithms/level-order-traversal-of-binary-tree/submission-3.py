# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque # import deque for O(1) popping from front of queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # naive brute force solution: iterate over the node and all its children possibly a O(n^2) or worse time complexity
        # better solution in this case, use BFS to visit all neighbors first and group them by their level before appending the level as a list inside the result list. O(n) linear time

        if not root:
            return []
        
        res = [] # final array retuned with houses the grouped levels: O(levels) space
        queue = deque([root]) # at some point houses all nodes: O(n)

        while queue: # views all nodes (n) -> O(n)
            level = [] # array that holds all nodes in the current level
            for i in range(len(queue)): # O(k), k = length of queue at each level < n
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        
        return res
    
    # runtime: O(n) * O(k) = O(n)??, space = O(n) + O(levels) = O(n)??
