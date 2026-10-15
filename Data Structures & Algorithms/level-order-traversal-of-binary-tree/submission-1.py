# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = []
        vals = []
        queue.append(root)
        vals.append(root.val)

        while queue:
            n = len(queue)
            res.append(list(vals))
            for i in range(n):
                node = queue.pop(0)
                vals.pop(0)
                if node.left:
                    queue.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    vals.append(node.right.val)

        return res
