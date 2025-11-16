class Solution:
    def numSub(self, s: str) -> int:
        M=10**9+7
        one=0
        ans=0
        for i in range(len(s)):
            if s[i]=='1':
                one+=1
                ans+=one
            else:
                one=0
        return ans%M