class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)


        for num, count in freq.items():
            if count == 1:
                return num

        return -1