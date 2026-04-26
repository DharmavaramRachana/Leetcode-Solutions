class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c, parent_r, parent_c, char):
            visit.add((r, c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr == rows or nc < 0 or nc == cols:
                    continue

                if grid[nr][nc] != char:
                    continue

                if nr == parent_r and nc == parent_c:
                    continue

                if (nr, nc) in visit:
                    return True

                if dfs(nr, nc, r, c, char):
                    return True

            return False

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit:
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True

        return False