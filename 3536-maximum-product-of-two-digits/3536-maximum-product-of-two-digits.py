class Solution:
    def maxProduct(self, n: int) -> int:
        firstmax=0
        secondmax=0
        while n:
            x=n%10
            if x>firstmax:
                secondmax=firstmax
                firstmax=x
            elif x>secondmax:
                secondmax=x
            n//=10
        return firstmax*secondmax