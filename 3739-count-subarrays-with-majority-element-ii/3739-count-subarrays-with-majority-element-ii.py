class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        size = 2 * n + 5
        offset = n + 2
        
        bit = [0] * (size + 1)

        def update(i):
            while i <= size:
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        ans = 0
        prefix = 0

        update(offset) 

        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1

            
            ans += query(prefix + offset - 1)
            update(prefix + offset)

        return ans