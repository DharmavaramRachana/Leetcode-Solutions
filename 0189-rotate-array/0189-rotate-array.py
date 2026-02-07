class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        k = k % len(nums) #If k > length of array, rotating by k is same as rotating by k % len(nums)Example: rotating by 10 in array of size 7 is same as rotating by 3.
        l, r = 0, len(nums) - 1

        while l < r :    # first reverse the array
            nums[l] , nums[r] = nums[r], nums[l]
            l,r = l + 1, r - 1


        l, r = 0, k -1
        while l < r : # bext reverse the first k elements
            nums[l] , nums[r] = nums[r], nums[l]
            l,r = l + 1, r - 1


        l, r = k, len(nums) -1 
        while l < r : # next remaining k elements
            nums[l] , nums[r] = nums[r], nums[l]
            l,r = l + 1, r - 1



        