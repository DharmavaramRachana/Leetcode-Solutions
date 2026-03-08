class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        res = 0

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        # 1. Skip spaces
        while i < n and s[i] == " ":
            i += 1

        # 2. Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Read digits
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. Overflow check
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + digit
            i += 1

        return sign * res