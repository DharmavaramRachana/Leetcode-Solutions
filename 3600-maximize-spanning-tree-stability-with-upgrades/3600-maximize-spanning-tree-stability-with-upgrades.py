class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.r = [0] * n
        self.comp = n

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.r[pa] < self.r[pb]:
            pa, pb = pb, pa
        self.p[pb] = pa
        if self.r[pa] == self.r[pb]:
            self.r[pa] += 1
        self.comp -= 1
        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # First verify mandatory edges do not already create a cycle
        dsu = DSU(n)
        for u, v, s, must in edges:
            if must == 1:
                if not dsu.union(u, v):
                    return -1

        vals = set()
        for _, _, s, must in edges:
            vals.add(s)
            if must == 0:
                vals.add(2 * s)

        vals = sorted(vals)
        if not vals:
            return -1

        def can(x: int) -> bool:
            d = DSU(n)
            upgrades = 0

            # mandatory edges must be included
            for u, v, s, must in edges:
                if must == 1:
                    if s < x:
                        return False
                    d.union(u, v)

            # use free optional edges first
            for u, v, s, must in edges:
                if must == 0 and s >= x:
                    d.union(u, v)

            # then edges that need upgrade
            for u, v, s, must in edges:
                if must == 0 and s < x and 2 * s >= x:
                    if d.union(u, v):
                        upgrades += 1
                        if upgrades > k:
                            return False

            return d.comp == 1

        lo, hi = 0, len(vals) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(vals[mid]):
                ans = vals[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
        