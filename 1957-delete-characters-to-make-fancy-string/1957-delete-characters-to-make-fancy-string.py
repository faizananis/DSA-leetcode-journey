class Solution:
    def makeFancyString(self, s: str) -> str:
        count=0
        res=s[0]
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                count+=1
            else:
                count=0
            if count==2:
                count-=1
                continue
            res+=s[i]
        return res