class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out = [0] * (n+1)
        inn = [0] * (n+1)

        for src, dst in trust:
            out[src] += 1
            inn[dst] += 1

        for i in range(1, n+1):
            if out[i] == 0 and inn[i] == n-1:
                return i

        return -1