class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []

        cur_sum = 0

        for n in nums:
            cur_sum += n
            res.append(cur_sum)

        return res

