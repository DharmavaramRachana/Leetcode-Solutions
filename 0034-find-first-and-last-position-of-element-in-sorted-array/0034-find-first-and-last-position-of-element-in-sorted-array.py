class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findLeft():
            l = 0
            r = len(nums) - 1
            res = -1

            while l <= r:

                m = (l + r) // 2

                if nums[m] == target:
                    res = m
                    r = m - 1

                elif nums[m] < target:
                    l = m + 1

                else:
                    r = m - 1

            return res

        def findRight():
            l = 0
            r = len(nums) - 1
            res = -1

            while l <= r:

                m = (l + r) // 2

                if nums[m] == target:
                    res = m
                    l = m + 1

                elif nums[m] < target:
                    l = m + 1

                else:
                    r = m - 1

            return res

        return [findLeft(), findRight()]


        

                
        