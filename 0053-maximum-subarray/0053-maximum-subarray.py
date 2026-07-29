class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        cursum = 0

        for n in nums:
            if cursum < 0:
                cursum = 0

            cursum += n

            max_sum = max(cursum, max_sum)

        return max_sum