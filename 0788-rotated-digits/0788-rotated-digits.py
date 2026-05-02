class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {0, 1, 2, 5, 6, 8, 9}
        change = {2, 5, 6, 9}

        count = 0

        for x in range(1, n + 1):
            num = x
            is_valid = True
            is_good = False

            while num > 0:
                digit = num % 10

                if digit not in valid:
                    is_valid = False
                    break

                if digit in change:
                    is_good = True

                num //= 10

            if is_valid and is_good:
                count += 1

        return count