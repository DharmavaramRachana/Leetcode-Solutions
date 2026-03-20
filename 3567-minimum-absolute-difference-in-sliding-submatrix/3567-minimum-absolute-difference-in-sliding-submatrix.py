class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = m - k + 1
        cols = n - k + 1
        
        ans = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                vals = set()
                
                # collect distinct values in this k x k submatrix
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        vals.add(grid[r][c])
                
                # if all values same (or only one element), answer is 0
                if len(vals) <= 1:
                    ans[i][j] = 0
                    continue
                
                arr = sorted(vals)
                
                best = float('inf')
                for x in range(1, len(arr)):
                    best = min(best, arr[x] - arr[x - 1])
                
                ans[i][j] = best
        
        return ans 