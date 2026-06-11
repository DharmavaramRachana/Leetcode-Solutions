class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1

        if n == 1:
            return 0

        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        max_depth = 0
        stack = [(1, 0, 0)]  # node, parent, depth

        while stack:
            node, parent, depth = stack.pop()
            max_depth = max(max_depth, depth)

            for nei in g[node]:
                if nei != parent:
                    stack.append((nei, node, depth + 1))

        return pow(2, max_depth - 1, MOD)