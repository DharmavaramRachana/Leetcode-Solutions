class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
       
        pairs = sorted(zip(robots, distance))
        robots = [p for p, _ in pairs]
        distance = [d for _, d in pairs]

        walls.sort()

        n = len(robots)

       
        def count_walls(L, R):
            if L > R:
                return 0
            return bisect_right(walls, R) - bisect_left(walls, L)

       
        intervals = [[None, None] for _ in range(n)]
        cnt = [[0, 0] for _ in range(n)]

        for i in range(n):
            prev_robot = robots[i - 1] if i > 0 else float("-inf")
            next_robot = robots[i + 1] if i + 1 < n else float("inf")

            # Left interval
            L1 = max(robots[i] - distance[i], prev_robot)
            R1 = robots[i]
            intervals[i][0] = (L1, R1)
            cnt[i][0] = count_walls(L1, R1)

            # Right interval
            L2 = robots[i]
            R2 = min(robots[i] + distance[i], next_robot)
            intervals[i][1] = (L2, R2)
            cnt[i][1] = count_walls(L2, R2)

        
        overlap = [[[0, 0], [0, 0]] for _ in range(n - 1)]

        for i in range(n - 1):
            for a in range(2):
                l1, r1 = intervals[i][a]
                for b in range(2):
                    l2, r2 = intervals[i + 1][b]
                    L = max(l1, l2)
                    R = min(r1, r2)
                    overlap[i][a][b] = count_walls(L, R)

       
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = cnt[0][0]
        dp[0][1] = cnt[0][1]

        for i in range(1, n):
            for b in range(2):
                best = 0
                for a in range(2):
                    best = max(best, dp[i - 1][a] - overlap[i - 1][a][b])
                dp[i][b] = cnt[i][b] + best

        return max(dp[n - 1][0], dp[n - 1][1])