class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        suffix_min = [float("inf")] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        ans = [0] * n
        start = 0
        curr_max = float("-inf")

        for i in range(n):
            curr_max = max(curr_max, nums[i])

            
            if i == n - 1 or curr_max <= suffix_min[i + 1]:
                for j in range(start, i + 1):
                    ans[j] = curr_max

                start = i + 1
                curr_max = float("-inf")

        return ans