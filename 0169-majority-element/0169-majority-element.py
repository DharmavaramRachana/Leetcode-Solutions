class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)

        for i in s :
            if nums.count(i) > len(nums) //2:

               return i