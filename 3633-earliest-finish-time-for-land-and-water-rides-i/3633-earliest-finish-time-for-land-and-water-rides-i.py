class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        res = float('inf')

        # land -> water
        for i in range(n):
            land_finish = max(landStartTime[i], 0) + landDuration[i]
            for j in range(m):
                start_water = max(land_finish, waterStartTime[j])
                water_finish = start_water + waterDuration[j]
                res = min(res, water_finish)

        # water -> land
        for j in range(m):
            water_finish = max(waterStartTime[j], 0) + waterDuration[j]
            for i in range(n):
                start_land = max(water_finish, landStartTime[i])
                land_finish = start_land + landDuration[i]
                res = min(res, land_finish)

        return res