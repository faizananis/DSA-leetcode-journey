class Solution:
    def totalMoney(self, n: int) -> int:
        total=28
        count=0
        div=n//7
        rem=n%7
        res=0
        for i in range(div):
            res+=total+7*i
            count+=1
        for i in range(1,rem+1):
            res+=i+count
        return res