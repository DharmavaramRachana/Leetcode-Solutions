class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        def reverse_num(x:int) -> int:
            return int(str(x)[::-1])

        index_map = {} #prev_reversed_value -> index
        res = float("inf")

        for i, a in enumerate(nums):

            if a in index_map:
                res = min(res, i - index_map[a])


            index_map[reverse_num(a)] = i

        return res if res != float("inf") else -1

        