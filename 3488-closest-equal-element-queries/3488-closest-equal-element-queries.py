class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        positions = defaultdict(list)

        # Store all indices for each value
        for i, num in enumerate(nums):
            positions[num].append(i)

        ans = []

        for q in queries:
            value = nums[q]
            inds = positions[value]

            # No other same value exists
            if len(inds) == 1:
                ans.append(-1)
                continue

            # Find q inside inds
            k = bisect_left(inds, q)

            prev_idx = inds[k - 1]                  # previous occurrence
            next_idx = inds[(k + 1) % len(inds)]   # next occurrence

            d1 = abs(q - prev_idx)
            d2 = abs(q - next_idx)

            # Circular distance
            d1 = min(d1, n - d1)
            d2 = min(d2, n - d2)

            ans.append(min(d1, d2))

        return ans