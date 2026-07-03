class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indeg = [0] * n
        max_cost = 0

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indeg[v] += 1
            max_cost = max(max_cost, cost)

        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)

            for v, cost in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def can(min_score):
            dist = [float('inf')] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == float('inf'):
                    continue

                for v, cost in graph[u]:
                    if cost < min_score:
                        continue
                    if v != n - 1 and not online[v]:
                        continue

                    if dist[u] + cost < dist[v]:
                        dist[v] = dist[u] + cost

            return dist[n - 1] <= k

        left, right = 0, max_cost
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans