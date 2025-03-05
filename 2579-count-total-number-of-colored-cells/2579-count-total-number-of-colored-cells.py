class Solution:
    def coloredCells(self, n: int) -> int:
        ans=1
        for i in range(2,n+1):
            ans+=2**i
        if n>3:
            ans-=2**(n-2)
        return ans