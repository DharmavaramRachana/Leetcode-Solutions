from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x: int) -> int:
            if x < 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            @lru_cache(None)
            def dfs(pos, tight, started, prev1, prev2, length):
                if pos == n:
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            False,
                            0,
                            0,
                            0
                        )
                        total_cnt += cnt
                        total_wav += wav
                        continue

                    if not started:
                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            True,
                            d,
                            0,
                            1
                        )
                        total_cnt += cnt
                        total_wav += wav
                        continue

                    add = 0
                    if length >= 2:
                        if ((prev1 > prev2 and prev1 > d) or
                            (prev1 < prev2 and prev1 < d)):
                            add = 1

                    cnt, wav = dfs(
                        pos + 1,
                        ntight,
                        True,
                        d,
                        prev1,
                        min(2, length + 1)
                    )

                    total_cnt += cnt
                    total_wav += wav + add * cnt

                return (total_cnt, total_wav)

            return dfs(0, True, False, 0, 0, 0)[1]

        return solve(num2) - solve(num1 - 1)