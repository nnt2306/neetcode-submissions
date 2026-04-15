class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) -1 
        max_water = 0 
        while start <end:
            water_amount = (end-start) * min(heights[start],heights[end])
            max_water = max(max_water,water_amount)
            if heights[start] <= heights[end]:
                start +=1
            else:
                end -=1
        return max_water

        