class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        i = 0

        while i < len(nums):
            total += nums[i]
            i +=1

        left_sum = 0
        i = 0

        while i < len(nums):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]
            i += 1

        return -1

        