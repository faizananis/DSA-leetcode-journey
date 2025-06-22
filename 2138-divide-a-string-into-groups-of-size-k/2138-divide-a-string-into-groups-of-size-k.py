class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        count=0
        ans=[]
        st=""
        for i in range(len(s)):
            st+=s[i]
            count+=1
            if count==k:
                ans.append(st)
                st=""
                count=0
        if count<k and count>0:
            while count<k:
                st+=fill
                count+=1
            ans.append(st)
        return ans
