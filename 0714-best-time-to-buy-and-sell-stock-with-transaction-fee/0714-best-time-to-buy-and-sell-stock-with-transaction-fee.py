class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]

        for p in prices:
            cash = max(cash, hold+p - fee) # sell
            hold = max(hold, cash - p) # buy

        return cash

        