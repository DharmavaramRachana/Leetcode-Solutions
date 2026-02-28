class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        window_sum = 0
        i = 0

        while i < k:
            window_sum += nums[i]
            i += 1

        max_sum = window_sum

        i = k
        while i < n:
            window_sum += nums[i]
            window_sum -= nums[i - k]

            if window_sum > max_sum:
                max_sum = window_sum 

            i += 1

        return max_sum / k

        