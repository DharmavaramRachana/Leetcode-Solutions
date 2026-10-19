class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            capacity = (l + r) // 2

            days_needed = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = 0

                current_load += weight

            if days_needed <= days:
                r = capacity

            else:
                l = capacity + 1

        return l