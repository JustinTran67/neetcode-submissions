# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # trivial solution -> place all elements vis dfs/bfs traversal into a BST into a list, sort the list, and then return the k-1 index approx. O(n) + O(nlogn) = O(nlogn) solution
        # proposed solution: use a maxheap capped at size k so that the smallest 3 node values are always maintained within the heap. the root value of the heap will always be the kth smallest integer in the BST. possibly O(n) * O(logk) = O(nlogk)

        maxHeap = [] # O(k) space
        
        def dfs(node): # dfs runs O(n) * O(logk) = O(nlogk)
            if not node:
                return
            else:
                heapq.heappush_max(maxHeap, node.val) # O(logk)
                while len(maxHeap) > k:
                    heapq.heappop_max(maxHeap) # O(logk)
            dfs(node.left)
            dfs(node.right)
            return node
        
        dfs(root)
        return maxHeap[0]

        # total time: O(nlogk), total space: heap O(k) + recursion stack O(h) = O(h) where balanced tree would mean space = O(logn), worst case degenerate trees mean space = O(n)