class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        size = n * m

        # Flatten the grid
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j] % MOD)

        # Prefix products
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD

        # Suffix products
        suffix = [1] * size
        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD

        # Build answer matrix
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                idx = i * m + j
                ans[i][j] = (prefix[idx] * suffix[idx]) % MOD

        return ans
        