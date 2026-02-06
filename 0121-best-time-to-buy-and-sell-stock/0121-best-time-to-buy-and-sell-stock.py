class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0  # buying index
        max_profit = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r  # new minimum (buy here)
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)

        return max_profit
