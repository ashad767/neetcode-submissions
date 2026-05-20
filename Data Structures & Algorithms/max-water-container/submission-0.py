class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            minHeight = min(heights[left], heights[right])

            width = right - left
            maximum = max(width * minHeight, maximum)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maximum