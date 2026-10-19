class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        while l < r:
            limit = (l + r) // 2
            parts = 1
            current_sum = 0

            for n in nums:

                if current_sum + n > limit:
                    parts += 1
                    current_sum = 0

                current_sum += n

            if parts <= k:
                r = limit

            else:
                l = limit + 1

        return l

