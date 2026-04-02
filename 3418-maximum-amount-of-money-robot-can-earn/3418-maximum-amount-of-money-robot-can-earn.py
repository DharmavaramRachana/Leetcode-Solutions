class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG = float('-inf')

        
        dp = [[[NEG] * 3 for _ in range(n)] for _ in range(m)]

        val = coins[0][0]
        if val >= 0:
            dp[0][0][0] = val
        else:
            dp[0][0][0] = val       
            dp[0][0][1] = 0        

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                val = coins[i][j]

                for k in range(3):
                    best_prev = NEG

                    if i > 0:
                        best_prev = max(best_prev, dp[i - 1][j][k])
                    if j > 0:
                        best_prev = max(best_prev, dp[i][j - 1][k])

                    
                    if best_prev != NEG:
                        dp[i][j][k] = max(dp[i][j][k], best_prev + val)

                    
                    if val < 0 and k > 0:
                        best_prev_neutral = NEG
                        if i > 0:
                            best_prev_neutral = max(best_prev_neutral, dp[i - 1][j][k - 1])
                        if j > 0:
                            best_prev_neutral = max(best_prev_neutral, dp[i][j - 1][k - 1])

                        if best_prev_neutral != NEG:
                            dp[i][j][k] = max(dp[i][j][k], best_prev_neutral)

        return max(dp[m - 1][n - 1])