class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # Build heights of consecutive 1s
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        ans = 0

        # For each row, sort heights descending
        for row in matrix:
            heights = sorted(row, reverse=True)

            # Try every possible width
            for width in range(1, n + 1):
                height = heights[width - 1]
                ans = max(ans, height * width)

        return ans