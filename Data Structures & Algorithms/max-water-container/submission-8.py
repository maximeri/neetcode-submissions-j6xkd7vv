class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            h, w = min(heights[l], heights[r]), r - l
            maxArea = max(maxArea, h * w)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -=1

        return maxArea