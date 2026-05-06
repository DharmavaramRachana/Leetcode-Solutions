class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        # Step 1: Rotate the box
        rotated = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = box[i][j]

        # Step 2: Apply gravity
        for col in range(m):
            empty_row = n - 1
            for row in range(n - 1, -1, -1):
                if rotated[row][col] == '*':
                    empty_row = row - 1
                elif rotated[row][col] == '#':
                    rotated[row][col] = '.'
                    rotated[empty_row][col] = '#'
                    empty_row -= 1

        return rotated