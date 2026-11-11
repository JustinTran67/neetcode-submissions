class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # top down (memoization)
        # m * n matrix: amount * index of (coins)
        # case amount 4, coins = [1, 2, 3]
        # dfs(0, 0) -> build up to 4 * 2, when populate table with repeated work
        # can make 2 decisions: pass value (4) - coins[index] with the same index and
        # pass value (4) - coins[index + 1] brute force would be O(2^n) -> dp would cut work to O(m * n) m being amount and n being len(coins) 
        dp = [[-1 for _ in range(len(coins))] for _ in range(amount + 1)] # we want the amount # included

        def dfs(value, index):
            if value == amount:
                return 1
            if value > amount or index >= len(coins):
                return 0
            if dp[value][index] != -1:
                return dp[value][index]
            
            dp[value][index] = dfs(value + coins[index], index) + dfs(value, index + 1)
            return dp[value][index]
        
        return dfs(0, 0)