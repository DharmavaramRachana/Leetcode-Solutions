class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        curr = 0

        for i in range(n):
            curr += i * nums[i]

        ans = curr

        for k in range(1, n):
            moved = nums[n-k]
            curr = curr+total - n * moved
            ans = max(ans, curr)

        return ans
