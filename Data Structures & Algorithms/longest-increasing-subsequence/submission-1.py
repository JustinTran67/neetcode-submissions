class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom up (clever)
        dp = [1] * len(nums) # start from end so init to 1

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)): # everything to the right of i
                if nums[i] < nums[j]: # Oncly calculate when strictly increasing, else reset the subsequence by leaving it (the new end) as 1
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp) # greatest value in dp is the length of longest subsequence strictly increasing
        
