class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = min(nums)
        largest = max(nums)

        exisiting = set(nums)

        missing = []

        for num in range(smallest, largest+1):
            if num not in exisiting:
                missing.append(num)

        return missing