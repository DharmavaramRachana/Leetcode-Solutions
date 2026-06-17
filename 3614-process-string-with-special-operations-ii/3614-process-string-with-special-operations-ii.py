class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        L = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                L += 1
            elif ch == '*':
                if L > 0:
                    L -= 1
            elif ch == '#':
                L *= 2
            elif ch == '%':
                pass
            lengths.append(L)

        if k < 0 or k >= L:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            cur = lengths[i]
            prev = lengths[i - 1] if i > 0 else 0

            if 'a' <= ch <= 'z':
                if k == cur - 1:
                    return ch
                # otherwise k stays the same

            elif ch == '*':
                # surviving characters keep the same index
                pass

            elif ch == '#':
                if prev > 0:
                    k %= prev

            elif ch == '%':
                k = cur - 1 - k

        return '.'