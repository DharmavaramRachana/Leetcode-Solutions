class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z0 = s.count('0')

        if z0 == 0:
            return 0
        if k == 0:
            return -1
        if k > n:
            return -1
        if k % 2 == 0 and z0 % 2 == 1:
            return -1

        # DSU "next unvisited" for each parity.
        # parent[p][i] = smallest unremoved index >= i with parity p, skipping by +2.
        parent = [[i for i in range(n + 2)] for _ in range(2)]

        def find(p: int, x: int) -> int:
            # Return next available index >= x with parity p.
            if x > n:
                return n + 1
            if x % 2 != p:
                x += 1
                if x > n:
                    return n + 1
            # Path compression
            if parent[p][x] != x:
                parent[p][x] = find(p, parent[p][x])
            return parent[p][x]

        def remove(p: int, x: int) -> None:
            # Mark x as visited: link it to the next candidate of same parity.
            parent[p][x] = find(p, x + 2)

        dist = [-1] * (n + 1)
        q = deque([z0])
        dist[z0] = 0
        remove(z0 % 2, z0)

        while q:
            z = q.popleft()
            d = dist[z]

            # compute feasible a range
            a_min = max(0, k - (n - z))
            a_max = min(k, z)
            if a_min > a_max:
                continue

            lo = z + k - 2 * a_max
            hi = z + k - 2 * a_min
            lo = max(lo, 0)
            hi = min(hi, n)

            p = (z + k) & 1  # parity of reachable states

            x = find(p, lo)
            while x <= hi:
                dist[x] = d + 1
                if x == 0:
                    return dist[x]
                q.append(x)
                remove(p, x)
                x = find(p, x)

        return -1
        