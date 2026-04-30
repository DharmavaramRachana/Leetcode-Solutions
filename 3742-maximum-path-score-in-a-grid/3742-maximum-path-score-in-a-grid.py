class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def cost(x):
            return 0 if x == 0 else 1

        dp = [[-1] * (k + 1) for _ in range(n)]

        start_cost = cost(grid[0][0])
        if start_cost <= k:
            dp[0][start_cost] = grid[0][0]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                val = grid[r][c]
                curr_cost = cost(val)

                new = [-1] * (k + 1)

                for used in range(curr_cost, k + 1):
                    prev_cost = used - curr_cost

                    best = -1

                    # from top
                    if r > 0:
                        best = max(best, dp[c][prev_cost])

                    # from left
                    if c > 0:
                        best = max(best, dp[c - 1][prev_cost])

                    if best != -1:
                        new[used] = best + val

                dp[c] = new

        ans = max(dp[n - 1])
        return ans if ans != -1 else -1