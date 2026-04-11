class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)

        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = float('inf')

        for indices in pos.values():
            if len(indices) < 3:
                continue

            for i in range(len(indices) - 2):
                ans = min(ans, 2 * (indices[i + 2] - indices[i]))

        return ans if ans != float('inf') else -1