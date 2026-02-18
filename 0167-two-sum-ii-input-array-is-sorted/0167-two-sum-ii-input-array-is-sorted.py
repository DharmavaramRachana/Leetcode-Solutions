class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        cursum = 0

        while l < r:
            cursum = nums[l] + nums[r]

            if cursum < target:
                l += 1

            elif cursum > target:
                r -= 1

            else:
                return [l+1, r+1]


        return []
            
        