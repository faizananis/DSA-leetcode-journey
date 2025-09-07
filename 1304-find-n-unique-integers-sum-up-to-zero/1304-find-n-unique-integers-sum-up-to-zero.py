class Solution:
    def sumZero(self, n: int) -> List[int]:
        zero=0
        arr=[]
        if n%2==1:
            zero=1
        for i in range(1,n//2+1):
            arr.append(-i)
        if zero:
            arr.append(0)
        for i in range(1,n//2+1):
            arr.append(i)
        return arr