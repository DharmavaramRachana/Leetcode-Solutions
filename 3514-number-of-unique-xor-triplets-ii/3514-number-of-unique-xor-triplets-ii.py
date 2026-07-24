class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums = set(nums)
        possible = {0}

        # Select exactly three numbers
        for _ in range(3):
            next_possible = set()

            for current_xor in possible:
                for num in nums:
                    next_possible.add(current_xor ^ num)

            possible = next_possible

        return len(possible)