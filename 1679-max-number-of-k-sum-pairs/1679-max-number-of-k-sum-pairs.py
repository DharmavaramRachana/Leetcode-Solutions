class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        ops = 0
        i = 0

        while i < len(nums):
            x = nums[i]
            need = k - x

            if need in freq and freq[need] > 0:
                freq[need] -= 1
                ops += 1

            else:
                if x in freq:
                    freq[x] += 1

                else:
                    freq[x] = 1

            i += 1

        return ops

        