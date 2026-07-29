class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_height = 0

        while l <= r:
            width = r - l
            h = min(height[l], height[r])
            max_height = max(max_height , width * h)
            if height[l] > height[r]:
                r -= 1

            else:
                l += 1

        return max_height
        