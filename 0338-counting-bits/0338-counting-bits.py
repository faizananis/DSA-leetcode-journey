class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            binary=bin(i)[2:]
            count=0
            for n in binary:
                if n=='1':
                    count+=1
            ans.append(count)
        return ans