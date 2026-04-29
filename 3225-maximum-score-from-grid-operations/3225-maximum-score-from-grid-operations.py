class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if n == 1:
            return 0

        
        prefix = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(n):
                prefix[c][r + 1] = prefix[c][r] + grid[r][c]

        def one_side_score(c, own, nei):
            if nei <= own:
                return 0
            return prefix[c][nei] - prefix[c][own]

        
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        
        for h0 in range(n + 1):
            for h1 in range(n + 1):
                dp[h0][h1] = one_side_score(0, h0, h1)

        NEG = -10**30

        for c in range(2, n):
            new_dp = [[NEG] * (n + 1) for _ in range(n + 1)]

            # we are calculating score for column c-1
            P = prefix[c - 1]

            for mid in range(n + 1):
                # arr[left] = dp[left][mid]
                arr = [dp[left][mid] for left in range(n + 1)]

                pref = [NEG] * (n + 1)
                pref[0] = arr[0]
                for i in range(1, n + 1):
                    pref[i] = max(pref[i - 1], arr[i])

                suff = [NEG] * (n + 2)
                for i in range(n, -1, -1):
                    suff[i] = max(suff[i + 1], arr[i] + P[i])

                for right in range(n + 1):
                    if right > mid:
                        best = pref[right] + P[right] - P[mid]
                        best = max(best, suff[right + 1] - P[mid])
                    else:
                        best = pref[mid]
                        best = max(best, suff[mid + 1] - P[mid])

                    new_dp[mid][right] = best

            dp = new_dp

        ans = 0

        
        last = n - 1
        for left in range(n + 1):
            for cur in range(n + 1):
                ans = max(ans, dp[left][cur] + one_side_score(last, cur, left))

        return ans