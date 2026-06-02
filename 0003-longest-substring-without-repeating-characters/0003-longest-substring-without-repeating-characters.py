class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            seen = set()

            for j in range(i, n):
                if s[j] in seen:
                    break

                seen.add(s[j])
                res = max(res, j - i + 1)

        return res