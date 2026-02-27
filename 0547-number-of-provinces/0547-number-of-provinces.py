class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = set()
        province = 0

        def dfs(city):
            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in visit:
                    visit.add(nei)
                    dfs(nei)


        for city in range(n):
            if city not in visit:
                province += 1
                visit.add(city)
                dfs(city)

        return province