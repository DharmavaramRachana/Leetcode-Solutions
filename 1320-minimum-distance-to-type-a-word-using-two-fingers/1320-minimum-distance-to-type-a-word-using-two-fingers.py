class Solution:
    def minimumDistance(self, word: str) -> int:
        def pos(ch):
            x = ord(ch) - ord('A')
            return x // 6, x % 6

        def dist(a, b):
            if a == 26 or b == 26:   # 26 means finger not placed yet
                return 0
            r1, c1 = divmod(a, 6)
            r2, c2 = divmod(b, 6)
            return abs(r1 - r2) + abs(c1 - c2)

        n = len(word)
        nums = [ord(c) - ord('A') for c in word]

        # dp[a][b] = min cost when fingers are at letters a and b
        # 26 means "not used yet"
        dp = [[float('inf')] * 27 for _ in range(27)]
        dp[26][26] = 0

        for ch in nums:
            new_dp = [[float('inf')] * 27 for _ in range(27)]
            for f1 in range(27):
                for f2 in range(27):
                    if dp[f1][f2] == float('inf'):
                        continue

                    # use finger 1 to type current char
                    new_dp[ch][f2] = min(new_dp[ch][f2],
                                         dp[f1][f2] + dist(f1, ch))

                    # use finger 2 to type current char
                    new_dp[f1][ch] = min(new_dp[f1][ch],
                                         dp[f1][f2] + dist(f2, ch))
            dp = new_dp

        ans = float('inf')
        for i in range(27):
            for j in range(27):
                ans = min(ans, dp[i][j])

        return ans
        