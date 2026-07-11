class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete_components = 0

        for node in range(n):
            if visited[node]:
                continue

            stack = [node]
            visited[node] = True

            vertices = 0
            degree_sum = 0

            while stack:
                current = stack.pop()
                vertices += 1
                degree_sum += len(graph[current])

                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            if degree_sum == vertices * (vertices - 1):
                complete_components += 1

        return complete_components