class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zeros = 0
        best = 0

        r = 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1

            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1

                l += 1

            current_len = (r-l+1)
            if current_len > best:
                best = current_len

            r += 1

        return best - 1

        