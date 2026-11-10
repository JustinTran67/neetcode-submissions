class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top-down (memoization 2d)
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def dfs(i, j):
            if i >= n - 1 and j >= m - 1:
                return 1
            elif i >= n:
                return 0
            elif j >= m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return dp[i][j]

        return dfs(0, 0)
