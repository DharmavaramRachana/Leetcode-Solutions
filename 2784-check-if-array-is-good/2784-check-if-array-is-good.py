class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)

        if len(nums) != n + 1:
            return False

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for i in range(1, n):
            if count.get(i, 0) != 1:
                return False

        return count.get(n, 0) == 2