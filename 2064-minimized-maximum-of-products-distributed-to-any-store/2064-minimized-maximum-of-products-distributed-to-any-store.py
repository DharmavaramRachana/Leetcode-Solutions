class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(quantities)

        while left < right:
            mid = left + (right - left) // 2

            stores_needed = 0

            for quantity in quantities:
                stores_needed += (quantity + mid - 1) // mid

            if stores_needed <= n:
                right = mid
            else:
                left = mid + 1

        return left