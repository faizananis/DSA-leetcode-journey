class Solution:
    def canAssign(self,mid,n,quant):
        count=0
        for val in quant:
            count+=math.ceil(val/mid)
        return count<=n
    
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m=len(quantities)
        low=1
        high=max(quantities)
        mid=-1
        ans=math.inf

        while low<=high:
            mid=(low+high)//2
            if self.canAssign(mid,n,quantities):
                ans=min(ans,mid)
                high=mid-1
            else:
                low=mid+1
        return ans
        