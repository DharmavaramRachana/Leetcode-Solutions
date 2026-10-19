class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0

        while n > 0:
            if n % 2 == 0:
                n = n // 2

            else:
                operations += 1

                if n == 1:
                    break

                if n % 4 == 3:
                    n += 1

                else:
                    n -= 1

        return operations
        