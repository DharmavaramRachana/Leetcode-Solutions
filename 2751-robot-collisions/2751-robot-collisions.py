class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])

        
        robots.sort(key=lambda x: x[0])

        stack = []  
        for i in range(n):
            if robots[i][2] == 'R':
                stack.append(i)
            else:
               
                while stack and robots[i][1] > 0:
                    j = stack[-1]   

                    if robots[j][1] < robots[i][1]:
                        
                        robots[i][1] -= 1
                        robots[j][1] = 0
                        stack.pop()

                    elif robots[j][1] > robots[i][1]:
                        
                        robots[j][1] -= 1
                        robots[i][1] = 0

                    else:
                        
                        robots[j][1] = 0
                        robots[i][1] = 0
                        stack.pop()
                        break

       
        survivors = []
        robots.sort(key=lambda x: x[3])  

        for robot in robots:
            if robot[1] > 0:
                survivors.append(robot[1])

        return survivors
        