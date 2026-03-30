class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        curMax, globalMax = 0, 0

        while l < r:
            height = min(heights[l], heights[r])
            curMax = max(curMax, height * (r-l))
            globalMax = max(curMax, globalMax)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return globalMax
            