class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen1 = set(nums1)
        seen2 = set(nums2)

        res = []

        for n in seen1:
            if n in seen2:
                res.append(n)

        return res