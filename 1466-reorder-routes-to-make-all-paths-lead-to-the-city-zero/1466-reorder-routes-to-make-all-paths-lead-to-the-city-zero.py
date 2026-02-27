class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b,1))
            graph[b].append((a,0))

        visited = [False] * n
        visited[0] = True
        q = deque([0])
        changes = 0

        while q:
            node = q.popleft()

            for nei,cost in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    changes += cost
                    q.append(nei)

        return changes



        