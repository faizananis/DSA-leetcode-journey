class Solution:
    def mirrorDistance(self, n: int) -> int:
        num=n
        rev=0
        while num:
            rev*=10
            rev+=num%10
            num//=10
        return abs(n-rev)