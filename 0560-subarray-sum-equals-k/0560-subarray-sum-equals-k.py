class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        prefix_count = {0:1}
        prefix_sum = 0

        for n in nums:
            prefix_sum += n

            count += prefix_count.get(prefix_sum - k, 0)
            prefix_count[prefix_sum] = 1 + prefix_count.get(prefix_sum, 0)

        return count

