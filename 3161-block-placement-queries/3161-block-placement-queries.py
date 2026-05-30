from bisect import bisect_right
from sortedcontainers import SortedList


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & -idx

    def query(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res = max(res, self.bit[idx])
            idx -= idx & -idx
        return res


class Solution:
    def getResults(self, queries):
        mx = 0
        obstacles = []

        for q in queries:
            mx = max(mx, q[1])
            if q[0] == 1:
                obstacles.append(q[1])

        mx += 1

        s = SortedList([0, mx])
        for x in obstacles:
            s.add(x)

        bit = Fenwick(mx + 2)

        def add_gap(l, r):
            bit.update(r, r - l)

        for i in range(1, len(s)):
            add_gap(s[i - 1], s[i])

        ans = []

        for q in reversed(queries):
            if q[0] == 2:
                x, sz = q[1], q[2]

                idx = s.bisect_right(x) - 1
                p = s[idx]

                best = max(bit.query(p), x - p)
                ans.append(best >= sz)

            else:
                x = q[1]

                idx = s.index(x)
                left = s[idx - 1]
                right = s[idx + 1]

                add_gap(left, right)  # merged gap
                s.remove(x)

        return ans[::-1]