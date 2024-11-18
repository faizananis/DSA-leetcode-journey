class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[]
        sums=0
        m=1
        for i in range(n):
            m=1
            sums=0
            if k>0:
                while m<=k:
                    sums+=code[(i+m)%n]
                    m+=1
            elif k<0:
                while m<=-k:
                    sums+=code[(i-m)%n]
                    m+=1
            res.append(sums)
        return res
