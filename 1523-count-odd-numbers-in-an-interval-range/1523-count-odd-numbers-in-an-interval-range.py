class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff=high-low
        ans=diff//2
        if low%2==1 or high%2==1:
            ans+=1
        return ans