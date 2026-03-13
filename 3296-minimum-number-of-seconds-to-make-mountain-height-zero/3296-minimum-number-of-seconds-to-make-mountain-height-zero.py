class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_finish(T: int) -> bool:
            reduced = 0

            for w in workerTimes:
                k = (2 * T) // w
                x = (isqrt(1 + 4 * k) - 1) // 2
                reduced += x

                if reduced >= mountainHeight:
                    return True

            return False

        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left
        