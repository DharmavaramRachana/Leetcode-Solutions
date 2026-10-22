class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        graph = defaultdict(list)

        MOD = 10**9 + 7

        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        dist = [float("inf")] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        min_heap = [(0, 0)]

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if time > dist[node]:
                continue

            for nei, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[node]

                    heapq.heappush(min_heap, (new_time, nei))

                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD

        return ways[n-1]