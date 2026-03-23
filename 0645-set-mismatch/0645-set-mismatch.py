class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        missing = -1

        for x in nums:
            if nums[abs(x) - 1] < 0:
                duplicate = abs(x)

            else:
                nums[abs(x) - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1

        return [duplicate, missing]       
        