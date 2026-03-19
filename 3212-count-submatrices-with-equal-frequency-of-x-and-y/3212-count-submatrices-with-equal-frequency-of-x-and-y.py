class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        colX = [0] * n
        colY = [0] * n
        ans = 0

        for i in range(m):
            curX = 0
            curY = 0

            for j in range(n):
                if grid[i][j] == "X":
                    colX[j] += 1

                if grid[i][j] == "Y":
                    colY[j] += 1

                curX += colX[j]
                curY += colY[j]

                if curX == curY and curX > 0:
                    ans += 1

        return ans
