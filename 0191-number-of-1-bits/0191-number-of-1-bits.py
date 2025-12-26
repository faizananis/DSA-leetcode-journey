class Solution:
    def hammingWeight(self, n: int) -> int:
        num=bin(n)[2:]
        ans=0
        for bit in num:
            if bit=='1':
                ans+=1
        return ans
