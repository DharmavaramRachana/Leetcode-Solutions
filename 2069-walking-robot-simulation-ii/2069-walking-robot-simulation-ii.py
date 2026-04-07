class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = "East"
        self.perimeter = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        num %= self.perimeter

        if num == 0:
            num = self.perimeter

        for _ in range(num):
            if self.dir == "East":
                if self.x + 1 < self.w:
                    self.x += 1
                else:
                    self.dir = "North"
                    self.y += 1

            elif self.dir == "North":
                if self.y + 1 < self.h:
                    self.y += 1
                else:
                    self.dir = "West"
                    self.x -= 1

            elif self.dir == "West":
                if self.x - 1 >= 0:
                    self.x -= 1
                else:
                    self.dir = "South"
                    self.y -= 1

            else:  # South
                if self.y - 1 >= 0:
                    self.y -= 1
                else:
                    self.dir = "East"
                    self.x += 1
        

    def getPos(self) -> List[int]:
        return [self.x, self.y]

        

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()