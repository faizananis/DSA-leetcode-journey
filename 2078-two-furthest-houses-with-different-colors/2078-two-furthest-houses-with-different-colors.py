class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left=0
        right=len(colors)-1
        while right>=0 and colors[0]==colors[right]:
            right-=1
        ans=right
        right=len(colors)-1
        while left<len(colors) and colors[left]==colors[right]:
            left+=1
        ans=max(ans,right-left)
        return ans
        
            