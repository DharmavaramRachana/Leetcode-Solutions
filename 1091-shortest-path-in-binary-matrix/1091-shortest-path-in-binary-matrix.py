class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n  = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        q = deque([(0, 0, 1)])
        visit = {0, 0}

        while q:
            row, col, length = q.popleft()

            if row == n - 1 and col == n - 1:
                return length

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and grid[nr][nc] == 0
                    and (nr, nc) not in visit
                ):
                    visit.add((nr, nc))
                    q.append((nr, nc, length + 1))

        return -1


        