class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        maxx=0
        while l<=r:
            maxx=max(maxx, min(height[l],height[r])*(r-l)) # min(height[l],height[r])*(r-l): current area
            if height[l]>height[r]:
                r-=1
            elif height[l]<height[r]:
                l+=1
            else:
                l+=1
                r-=1
        return maxx
