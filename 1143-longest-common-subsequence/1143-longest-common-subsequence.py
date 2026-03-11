class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        prev = [0] * (n+1)

        for i in range(m-1, -1, -1):
            curr = [0] * (n+1)
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j+1]

                else:
                    curr[j] = max(prev[j], curr[j+1])

            prev = curr

        return prev[0]