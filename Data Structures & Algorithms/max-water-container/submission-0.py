class Solution:
    def maxArea(self, heights: List[int]) -> int:
       # Need to see the largest area
       # Need to keep track of the index of both to get the width
       max_area = 0
       l, r = 0, len(heights) - 1 
       # starting at the far left and right gives us the largest width
       # As we move inwards the width will decrease, but if the height is
       # larger than it is worth it, so keep track of the largest areas
       # and the the values associated with it
       # How do we know which one to move tho? Move the pointer with the smaller
       # height.
       while (l < r):
        area = min(heights[l], heights[r]) * (r - l)
        max_area = max(max_area, area)
        if (heights[l] < heights[r]):
            l+=1
        else:
            r-=1
       return max_area





        