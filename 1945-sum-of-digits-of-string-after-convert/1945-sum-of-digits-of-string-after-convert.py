class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number=0
        for i in s:
            if ord(i)<106:
                number=number*10
            else:
                number=number*100
            number+=ord(i)-96
        res=0
        while k>0:
            res=0
            while number>0:
                res+=number%10
                number=number//10
            number=res
            k-=1
        return res
