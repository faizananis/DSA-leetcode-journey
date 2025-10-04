class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        area=0
        maxArea=0
        max1=0
        max2=0
        while left<right:
            max1=max(max1,height[left])
            max2=max(max2,height[right])
            area=min(max1,max2)*(right-left)
            maxArea=max(maxArea,area)
            if max1<max2:
                left+=1
            else:
                right-=1
        return maxArea





        