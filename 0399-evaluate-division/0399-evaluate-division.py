class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        # build graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))

        def dfs(src: str, dst: str, visited: set) -> float:
            if src == dst:
                return 1.0

            visited.add(src)

            for nei, w in graph[src]:
                if nei in visited:
                    continue
                res = dfs(nei, dst, visited)
                if res != -1.0:
                    return w * res

            return -1.0

        ans = []
        for c, d in queries:
            if c not in graph or d not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(c, d, set()))
        return ans
