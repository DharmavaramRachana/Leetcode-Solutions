class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        res = []
        cycle = set()
        visit = set()

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True

            
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False

            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False :
                return []

        return res
