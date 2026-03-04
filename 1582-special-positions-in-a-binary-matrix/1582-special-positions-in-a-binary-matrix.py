class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        rowSum = [0] * m
        colSum = [0] * n

        # Count 1s in each row and column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rowSum[i] += 1
                    colSum[j] += 1

        # Count special positions
        ans = 0
        for i in range(m):
            if rowSum[i] != 1:
                continue
            for j in range(n):
                if mat[i][j] == 1 and colSum[j] == 1:
                    ans += 1

        return ans
        