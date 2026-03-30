class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd1=[]
        even1=[]
        odd2=[]
        even2=[]

        for i in range(len(s1)):
            if i&1:
                odd1.append(s1[i])
                odd2.append(s2[i])
            else:
                even1.append(s1[i])
                even2.append(s2[i])
        
        return sorted(odd1)==sorted(odd2) and sorted(even1)==sorted(even2)