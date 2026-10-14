class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        best = 0
        for i in range(1, len(prices)):
            if prices[i] > buy:
                if (prices[i] - buy) > best:
                    best = prices[i] - buy
            else:
                buy = prices[i]
        return best