class Solution:
    def reverseDegree(self, s: str) -> int:
        sums=0
        for i in range(1,len(s)+1):
            val=ord(s[i-1])-97
            val=26-val
            sums+=val*i
        return sums