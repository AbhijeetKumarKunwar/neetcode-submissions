class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxArea=0
        while(l<r):
            minHeight=min(heights[l],heights[r])
            maxArea=max(minHeight*(r-l),maxArea)
            minPointer=min(heights[l],heights[r])
            if minPointer==heights[l]:
                l+=1
            else:
                r-=1
        return maxArea    

        