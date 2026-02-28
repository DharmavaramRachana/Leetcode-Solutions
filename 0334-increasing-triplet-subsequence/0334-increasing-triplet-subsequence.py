class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_number = float("inf")
        second_number = float("inf")
        for n in nums:
            if n <= first_number:
                first_number = n

            elif n <= second_number:
                second_number = n

            else:
                return True

        return False