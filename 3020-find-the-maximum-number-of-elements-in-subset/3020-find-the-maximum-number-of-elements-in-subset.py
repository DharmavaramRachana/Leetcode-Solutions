class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        # Special case for 1
        if 1 in freq:
            ans = max(ans, freq[1] if freq[1] % 2 == 1 else freq[1] - 1)

        for x in freq:
            if x == 1:
                continue

            cur = x
            length = 0

            while freq[cur] >= 2:
                length += 2
                cur = cur * cur

            if freq[cur] >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans