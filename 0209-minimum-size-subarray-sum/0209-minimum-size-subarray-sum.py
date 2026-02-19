class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float("infinity")

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(r-l+1, res)
                total -= nums[l]
                l += 1

        return res if res != float("infinity") else 0
        