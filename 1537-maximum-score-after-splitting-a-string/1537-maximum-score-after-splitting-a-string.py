class Solution:
    def maxScore(self, s: str) -> int:
        zero=0
        one=0
        size=len(s)
        sums=0
        prefixLeft=[0]*size
        prefixRight=[0]*size
        nums=list(s)

        for i in range(size-1):
            if nums[i]=='0':
                zero+=1
            prefixLeft[i]=zero
        
        for j in range(size-1,0,-1):
            if nums[j]=='1':
                one+=1
            prefixRight[j]=one
        
        for i in range(size):
            sums=max(sums,prefixLeft[i]+prefixRight[i])
        
        return sums

        # for 

        # l=0
        # r=0


        # if s[0]=='0':
        #     zero+=1
        # for i in range(1,len(s)):
        #     if s[i]=='1':
        #         one+=1
        # res=max(zero+one,0)
        # while r<len(s)-2:
        #     r+=1
            
        #     if s[r]=='0':
        #         zero+=1
        #     elif s[r]=='1':
        #         one-=1
        #     res=max(zero+one,res)
            
        # return(res)
        