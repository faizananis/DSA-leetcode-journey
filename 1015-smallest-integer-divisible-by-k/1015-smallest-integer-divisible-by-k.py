class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        num=0
        arr=[]
        for i in range(1,k+1):
            num*=10
            num+=1
            arr.append(num)
            if num%k==0:
                return i
        return -1
        

        