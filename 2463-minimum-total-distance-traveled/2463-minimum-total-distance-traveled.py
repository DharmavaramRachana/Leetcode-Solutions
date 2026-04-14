from functools import lru_cache
from math import inf
from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        m, n = len(robot), len(factory)

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            # all robots repaired
            if i == m:
                return 0

            # no factories left, but robots remain
            if j == n:
                return inf

            pos, limit = factory[j]

            # option 1: skip this factory
            ans = dp(i, j + 1)

            # option 2: assign up to 'limit' consecutive robots to this factory
            total = 0
            for k in range(1, min(limit, m - i) + 1):
                total += abs(robot[i + k - 1] - pos)
                ans = min(ans, total + dp(i + k, j + 1))

            return ans

        return dp(0, 0)