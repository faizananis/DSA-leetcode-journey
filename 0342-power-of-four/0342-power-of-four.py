class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num=bin(n)
        num=num[2:]
        count1=num.count('1')
        if count1!=1:
            return False
        count0=num.count('0')
        if n==1:
            return True
        if n>0 and count0>0 and count0%2==0:
            return True
        return False