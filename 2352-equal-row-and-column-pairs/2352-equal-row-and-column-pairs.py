class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowCount = {}

        for r in range(n):
            key = tuple(grid[r])
            rowCount[key] = 1 + rowCount.get(key , 0)
        
        ans = 0
        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
                ans += rowCount.get(tuple(col), 0)

        return ans

        