class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            vals = []

            top, bottom = layer, m - 1 - layer
            left, right = layer, n - 1 - layer

            # collect counter-clockwise order
            for c in range(left, right + 1):
                vals.append(grid[top][c])

            for r in range(top + 1, bottom + 1):
                vals.append(grid[r][right])

            for c in range(right - 1, left - 1, -1):
                vals.append(grid[bottom][c])

            for r in range(bottom - 1, top, -1):
                vals.append(grid[r][left])

            size = len(vals)
            rot = k % size

            # counter-clockwise rotation
            vals = vals[rot:] + vals[:rot]

            idx = 0

            # put back
            for c in range(left, right + 1):
                grid[top][c] = vals[idx]
                idx += 1

            for r in range(top + 1, bottom + 1):
                grid[r][right] = vals[idx]
                idx += 1

            for c in range(right - 1, left - 1, -1):
                grid[bottom][c] = vals[idx]
                idx += 1

            for r in range(bottom - 1, top, -1):
                grid[r][left] = vals[idx]
                idx += 1

        return grid