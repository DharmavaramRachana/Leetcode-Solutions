class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        return [
            [
                grid[((i * n + j - k) % total) // n]
                    [((i * n + j - k) % total) % n]
                for j in range(n)
            ]
            for i in range(m)
        ]