class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom-up (iterative)
        n = len(cost)
        if n <= 2: # constraint is that n is at least 2
            return min(cost[0], cost[1])
        dp = [0] * (n + 1) # might change back to n
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[n - 1], dp[n - 2])
