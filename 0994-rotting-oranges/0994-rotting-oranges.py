class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append((r,c))

        time = 0
        while q and fresh >0:
            for i in range(len(q)):
                row,col = q.popleft()

                directions = [[1,0],[0,1],[-1,0],[0,-1]]

                for dr,dc in directions:
                    r , c = row + dr , col + dc

                    if (r in range(rows) and c in range(cols) and grid[r][c] == 1):
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1

        


                    