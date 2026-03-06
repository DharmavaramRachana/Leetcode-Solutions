class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax , globalMin = nums[0], nums[0]
        curmax, curmin = 0, 0
        total = 0

        for n in nums:
            curmax = max(curmax+n, n)
            curmin = min(curmin+n, n)
            total += n

            globalMax = max(curmax,globalMax)
            globalMin = min(curmin, globalMin)

        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
        