class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        need = 1 << k  # 2^k

        # Quick impossible checks
        if n < k or (n - k + 1) < need:
            return False

        seen = bytearray(need)   # 0/1 flags, very compact + fast
        mask = need - 1

        val = 0
        # build first window
        for i in range(k):
            val = (val << 1) | (s[i] == '1')
        seen[val] = 1
        found = 1

        # slide windows
        for i in range(k, n):
            val = ((val << 1) & mask) | (s[i] == '1')
            if not seen[val]:
                seen[val] = 1
                found += 1
                if found == need:   # early exit as soon as complete
                    return True

        return False
        