class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r

            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)

        return max_profit
        