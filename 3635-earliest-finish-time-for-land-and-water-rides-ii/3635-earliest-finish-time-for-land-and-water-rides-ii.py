class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        min_land_finish = min(
            s + d for s, d in zip(landStartTime, landDuration)
        )

        min_water_finish = min(
            s + d for s, d in zip(waterStartTime, waterDuration)
        )

        ans = float('inf')

        # Land -> Water
        for ws, wd in zip(waterStartTime, waterDuration):
            ans = min(
                ans,
                max(ws, min_land_finish) + wd
            )

        # Water -> Land
        for ls, ld in zip(landStartTime, landDuration):
            ans = min(
                ans,
                max(ls, min_water_finish) + ld
            )

        return ans