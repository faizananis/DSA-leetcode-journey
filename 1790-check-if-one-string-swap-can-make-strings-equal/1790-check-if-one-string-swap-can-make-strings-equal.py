class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count=0
        temp1=[]
        temp2=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
                temp1.append(s1[i])
                temp2.append(s2[i])
            if count==3:
                return False
        if count==0:
            return True
        if len(temp1)==2 and temp1[0]==temp2[1] and temp1[1]==temp2[0]:
            return True
        return False