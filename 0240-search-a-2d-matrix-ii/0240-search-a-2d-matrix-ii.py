class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == target:
                    return True

        return False