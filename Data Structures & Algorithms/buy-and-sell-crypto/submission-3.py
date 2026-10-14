class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        best = 0
        for i in prices:
            best = max(best, i-buy)
            buy = min(buy, i)
        return best