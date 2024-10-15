class Solution:
    def minimumSteps(self, s: str) -> int:
        swap=0
        ones=0
        for c in s:
            if c == '0':
                swap+=ones
            else:
                ones+=1
        return swap

        # if(len(s)==1):
        #     return 0
        # c=s.count('0')
        # flag=False
        # j=0
        # s=list(s)
        # steps=0
        # while 1:
        #     flag=False
        #     for left in range(j,len(s)-1):
        #         right=left+1
        #         if s[left]=='1' and flag==False:
        #             j=left
        #             flag=True
        #         if s[left]=='1' and s[right]=='0':
        #             s[left]='0'
        #             s[right]='1'
        #             steps+=1
        #             break
        #     else:
        #         break
        # return steps 

