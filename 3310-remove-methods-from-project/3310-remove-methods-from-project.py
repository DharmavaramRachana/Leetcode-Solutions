from typing import List


class Solution:
    def remainingMethods(
        self,
        n: int,
        k: int,
        invocations: List[List[int]]
    ) -> List[int]:

        graph = [[] for _ in range(n)]

        for method_a, method_b in invocations:
            graph[method_a].append(method_b)

        suspicious = set()

        # Find every method reachable from the buggy method k
        def dfs(method):
            if method in suspicious:
                return

            suspicious.add(method)

            for invoked_method in graph[method]:
                dfs(invoked_method)

        dfs(k)

        # Check whether an outside method invokes a suspicious method
        for method_a, method_b in invocations:
            if method_a not in suspicious and method_b in suspicious:
                # Suspicious methods cannot be removed
                return list(range(n))

        # Remove all suspicious methods
        return [
            method
            for method in range(n)
            if method not in suspicious
        ]
        