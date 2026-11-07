class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom-up (iterative)
        n = len(nums)
        if n == 2: # constraint says n is at least 1
            return max(nums[0], nums[1])
        elif n < 2:
            return nums[0]
        
        dp = [0] * (n + 1)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            # dp[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
        
        return dp[n - 1]