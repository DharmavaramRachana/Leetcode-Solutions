class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key (i, buying) val = maxprofit

        def dfs(i, buying):
            # CHANGE 1: Must be >= to catch the end of the list
            if i >= len(prices):
                return 0

            # CHANGE 2: Fixed typo 'buyinhg' -> 'buying'
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # i + 2 logic handles the mandatory 1-day cooldown
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)
        