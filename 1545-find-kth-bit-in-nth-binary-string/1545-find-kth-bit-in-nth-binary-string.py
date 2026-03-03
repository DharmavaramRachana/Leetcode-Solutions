class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        mid = 1 << (n - 1)  # 2^(n-1), 1-indexed middle

        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n - 1, k)

        # k > mid: map to mirrored position in S(n-1) and invert
        mirrored = (1 << n) - k  # 2^n - k
        bit = self.findKthBit(n - 1, mirrored)
        return "1" if bit == "0" else "0"