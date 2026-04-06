class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set((x, y) for x, y in obstacles)

        # North, East, South, West
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  # start facing north

        x = y = 0
        ans = 0

        for cmd in commands:
            if cmd == -2:          # turn left
                d = (d - 1) % 4
            elif cmd == -1:        # turn right
                d = (d + 1) % 4
            else:                  # move forward cmd steps
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)

        return ans