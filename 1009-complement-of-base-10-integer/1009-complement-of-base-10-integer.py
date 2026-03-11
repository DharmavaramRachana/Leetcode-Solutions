class Solution:
    def bitwiseComplement(self, n: int) -> int:

        if n == 0:
            return 1
        result = 0
        bit = 1
        
        while n > 0:
            if (n & 1) == 0:
                result |= bit
            bit <<= 1
            n >>= 1
        
        return result