class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []

        for row in grid:
            for val in row:
                nums.append(val)

        rem = nums[0] % x
        for val in nums:
            if val % x != rem:
                return -1

        nums.sort()
        median = nums[len(nums) //2]

        ops = 0
        for val in nums:
            ops += abs(val - median) // x

        return ops