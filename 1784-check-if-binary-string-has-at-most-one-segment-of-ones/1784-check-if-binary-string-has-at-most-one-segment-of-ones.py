class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag=False
        for i in range(len(s)):
            if s[i]=='0':
                flag=True
            elif flag==True:
                return False
        return True

                