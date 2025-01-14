class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C=[0]*len(A)
        count=0
        s1=set()
        s2=set()
        for i in range(len(A)):
            s1.add(A[i])
            s2.add(B[i])
            if A[i]==B[i]:
                count+=1
            else:
                if A[i] in s2:
                    count+=1
                if B[i] in s1:
                    count+=1
            C[i]=count
        return C