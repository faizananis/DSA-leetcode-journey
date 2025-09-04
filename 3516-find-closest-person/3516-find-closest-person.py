class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        val1=abs(z-x)
        val2=abs(z-y)
        if val1==val2:
            return 0
        if val1<val2:
            return 1
        return 2