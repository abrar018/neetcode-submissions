import math
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        l,r = 0,len(heights)-1
        while l<r:
            v=min(heights[l],heights[r])*math.fabs(l-r)
            m=max(v,m)
            print(v,m)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return int(m)
