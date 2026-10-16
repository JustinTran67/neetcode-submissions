class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] != 1:
                return 0
            
            # sink so you dont recount old islands
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for r in range(R):
            for c in range(C):
                res = max(res, dfs(r, c))
            
        return res