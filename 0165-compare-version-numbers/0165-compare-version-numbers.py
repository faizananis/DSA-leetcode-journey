class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num=0
        i=0
        l1=[]
        l2=[]
        for i in range(len(version1)):
            if version1[i]=='.':
                l1.append(num)
                num=0
            else:
                num*=10
                num+=ord(version1[i])-48
        l1.append(num)
        num=0
        for i in range(len(version2)):
            if version2[i]=='.':
                l2.append(num)
                num=0
            else:
                num*=10
                num+=ord(version2[i])-48
        l2.append(num)
        i=0
        while i<len(l1) and i<len(l2):
            if l1[i]<l2[i]:
                return -1
            elif l1[i]>l2[i]:
                return 1
            i+=1
        while i<len(l1):
            if l1[i]!=0:
                return 1
            i+=1
        while i<len(l2):
            if l2[i]!=0:
                return -1
            i+=1
        return 0