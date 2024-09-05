class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        rolls_sum=sum(rolls)
        total_sum=mean*(m+n)
        missing_sum=total_sum-rolls_sum
        expected_sum=rolls_sum+n*6
        if expected_sum < total_sum or missing_sum<n*1:
            return []
        i=0
        val=1
        k=0
        missing_sum-=n
        mod=missing_sum%5
        floor_div=missing_sum//5
        ans=[6]*floor_div
        if len(ans)<n:
            ans.append(mod+1)
        if len(ans)<n:
            ans=ans+[1]*(n-len(ans))
        return ans
            


            
        
        
