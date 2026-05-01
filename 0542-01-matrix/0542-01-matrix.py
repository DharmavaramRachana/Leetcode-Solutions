class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m , n = len(mat), len(mat[0])
        large = m + n


        dist = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dist[i][j] = 0 if mat[i][j] == 0 else large

        for i in range(m):
            for j in range(n):
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)

       
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j < n - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)

        return dist