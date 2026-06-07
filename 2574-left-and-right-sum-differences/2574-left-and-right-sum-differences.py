class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        leftSum = 0
        ans = []

        for num in nums:
            rightSum = total - leftSum - num
            ans.append(abs(leftSum - rightSum))
            leftSum += num

        return ans