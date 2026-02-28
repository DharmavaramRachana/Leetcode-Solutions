class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 1000000007
        ans = 0
        bits = 0

        i = 1
        while i <= n:
            # if i is a power of two, bit-length increases
            if (i & (i - 1)) == 0:
                bits += 1

            ans = ((ans << bits) + i) % MOD
            i += 1

        return ans
        