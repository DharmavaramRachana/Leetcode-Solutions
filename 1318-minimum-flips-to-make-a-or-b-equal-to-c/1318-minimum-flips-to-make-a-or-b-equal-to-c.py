class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        diff = (a|b) ^ c

        while diff:
            bit = diff & 1 # if bit is 1 then change the bits

            if bit:
                if c & 1 == 0:
                    flips += (a & 1) + (b & 1)

                else:
                    flips += 1
                
            a >>= 1
            b >>= 1
            c >>= 1
            diff >>= 1

        return flips
        