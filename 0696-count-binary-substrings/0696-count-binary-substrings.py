class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_run = 0
        curr_run = 1
        ans = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_run += 1
            else:
                ans += min(prev_run, curr_run)
                prev_run = curr_run
                curr_run = 1

        ans += min(prev_run, curr_run)
        return ans
        