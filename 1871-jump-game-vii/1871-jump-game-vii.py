class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[-1] != '0':
            return False

        queue = [0]
        farthest = 0

        for i in queue:
            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    queue.append(j)

            farthest = max(farthest, end)

        return n == 1