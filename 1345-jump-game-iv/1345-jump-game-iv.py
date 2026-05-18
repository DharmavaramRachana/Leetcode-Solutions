class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n <= 1:
            return 0

        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        queue = deque([0])
        visited = set([0])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()

                if i == n - 1:
                    return steps

                neighbors = [i - 1, i + 1]

                for j in graph[arr[i]]:
                    neighbors.append(j)

                for nei in neighbors:
                    if 0 <= nei < n and nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

                # Important optimization
                graph[arr[i]].clear()

            steps += 1

        return -1