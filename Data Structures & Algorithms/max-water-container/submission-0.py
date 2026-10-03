class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l,r=0,n-1
        maxarea=0

        while(l<r):
            width=r-l
            height=min(heights[l],heights[r])
            maxarea=max(maxarea,height*width)

            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1
        return maxarea
        
        