class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number=0
        for i in s:
            if ord(i)<=105:
                number=number*10
            elif ord(i)<=122:
                number=number*100
            number=number+ord(i)-96
        
        while k>0:
            sume=0
            while number>0:
                sume=sume+number%10
                number=number//10
            number=sume
            k-=1
        return sume