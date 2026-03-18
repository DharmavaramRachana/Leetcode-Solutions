class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                top = grid[i-1][j] if i > 0 else 0
                left = grid[i][j-1] if j > 0 else 0
                dia = grid[i-1][j-1] if i > 0 and j > 0 else 0


                grid[i][j] = grid[i][j] + top + left - dia

                if grid[i][j] <= k:
                    count += 1

        return count