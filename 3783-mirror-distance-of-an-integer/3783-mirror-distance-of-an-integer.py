class Solution:
    def mirrorDistance(self, n: int) -> int:

        def reverse_sum(n:int)->int:
            sign = -1 if n < 0 else 1
            n = abs(n)
            rev = 0
            while n > 0:
                digit = n % 10
                rev = rev * 10 + digit
                n //= 10

            return sign * rev

        reverse_digit = reverse_sum(n)
        diff = abs(reverse_digit - n)

        return diff
        