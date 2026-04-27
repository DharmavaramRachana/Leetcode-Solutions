class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        directions = {
            1: [(0,-1), (0,1)],
            2: [(-1,0), (1,0)],
            3: [(0,-1), (1,0)],
            4: [(0,1), (1,0)],
            5: [(0,-1), (-1,0)],
            6: [(0,1), (-1,0)]
        }

        q = deque([(0, 0)])
        visit = set()
        visit.add((0, 0))

        while q:
            r, c = q.popleft()

            if r == rows - 1 and c == cols - 1:
                return True

            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        visit.add((nr, nc))
                        q.append((nr, nc))

        return False