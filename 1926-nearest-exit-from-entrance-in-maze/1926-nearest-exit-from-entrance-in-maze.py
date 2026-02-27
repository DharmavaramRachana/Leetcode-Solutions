class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
     
        rows, cols = len(maze), len(maze[0])
        sr, sc = entrance
        q = deque()
        q.append((sr,sc, 0)) #startr,startc,steps

        maze[sr][sc] = "+"
        directions = [[1,0],[0,1],[-1,0],[0,-1]]


        while q:
            r,c , steps = q.popleft()

            for dr,dc in directions:
                row, col = r + dr, c + dc

                if (0 <= row < rows and 0 <= col < cols):
                    if maze[row][col] == ".":
                        if (row == 0 or row == rows - 1 or col == 0 or col == cols-1):
                            return steps +1

                        maze[row][col] = "+"
                        q.append((row,col,steps+1))


        return -1


        