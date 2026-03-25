class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total = sum(sum(row) for row in grid)

        if total % 2 != 0:
            return False

        target = total // 2

        curr = 0
        for r in range(m-1):
            curr += sum(grid[r])
            if curr == target:
                return True

        col_sum = [0] * n
        for r in range(m):
            for c in range(n):
                col_sum[c] += grid[r][c]

        curr = 0
        for c in range(n - 1):  
            curr += col_sum[c]
            if curr == target:
                return True

        return False

        