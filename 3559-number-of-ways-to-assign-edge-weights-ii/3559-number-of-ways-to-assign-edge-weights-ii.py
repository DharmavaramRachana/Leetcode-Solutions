class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1

        # Build tree
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = (n).bit_length()

        depth = [0] * (n + 1)
        up = [[0] * LOG for _ in range(n + 1)]

        # DFS/BFS to fill depth and parent
        stack = [(1, 0)]
        while stack:
            node, parent = stack.pop()
            up[node][0] = parent

            for j in range(1, LOG):
                up[node][j] = up[up[node][j - 1]][j - 1]

            for nei in g[node]:
                if nei == parent:
                    continue
                depth[nei] = depth[node] + 1
                stack.append((nei, node))

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            for j in range(LOG):
                if diff & (1 << j):
                    a = up[a][j]

            if a == b:
                return a

            for j in range(LOG - 1, -1, -1):
                if up[a][j] != up[b][j]:
                    a = up[a][j]
                    b = up[b][j]

            return up[a][0]

        ans = []

        for u, v in queries:
            w = lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[w]

            if d == 0:
                ans.append(0)
            else:
                ans.append(pow(2, d - 1, MOD))

        return ans