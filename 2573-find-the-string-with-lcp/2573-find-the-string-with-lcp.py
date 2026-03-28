from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        # Step 1: merge positions that must have same starting character
        dsu = DSU(n)
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    dsu.union(i, j)

        # Step 2: build lexicographically smallest string
        group_to_char = {}
        next_char = ord('a')
        word = [''] * n

        for i in range(n):
            root = dsu.find(i)
            if root not in group_to_char:
                if next_char > ord('z'):
                    return ""  # more than 26 distinct groups
                group_to_char[root] = chr(next_char)
                next_char += 1
            word[i] = group_to_char[root]

        word = ''.join(word)

        # Step 3: verify by recomputing LCP matrix
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 0

                if dp[i][j] != lcp[i][j]:
                    return ""

        return word