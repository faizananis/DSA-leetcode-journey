class Solution:
    def hammingWeight(self, n: int) -> int:
        binary=bin(n)[2:]
        count=0
        for n in binary:
            if n=='1':
                count+=1
        return count