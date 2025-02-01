class Solution:
    def addDigits(self, num: int) -> int:
        sums=0
        while num>9:
            sums=0
            while num>0:
                sums+=num%10
                num//=10
            num=sums
        return num
        