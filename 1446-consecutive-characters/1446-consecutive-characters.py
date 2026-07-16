class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        max_count = 1
        cnt = 1

        for i in range(1, n):
            if s[i] == s[i-1]:
                cnt += 1

            else:
                cnt = 1

            if cnt > max_count:
                max_count = cnt

        return max_count
                
        