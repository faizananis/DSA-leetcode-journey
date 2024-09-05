class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        ans=[]
        m=len(rolls)
        rolls_sum=sum(rolls)
        total_sum=mean*(m+n)
        missing_sum=total_sum-rolls_sum
        expected_sum=rolls_sum+n*6
        if expected_sum < total_sum or missing_sum<n*1:
            return ans
        i=0
        val=1
        k=0
        while i<n:
            ans.append(1)
            i+=1
        i=0
        missing_sum-=n
        mod=missing_sum%5
        div=missing_sum//5
        while i<div:
            ans[i]=6
            i+=1
        if i<n:
            ans[i]+=mod
        return ans
        # while i<n:
        #     ans[i]+=1
        # while sum(ans)!=missing_sum:
        #     if k<n:
        #         ans.append(val)
        #         k+=1
        #     if val<=6:
            


            
        
        
