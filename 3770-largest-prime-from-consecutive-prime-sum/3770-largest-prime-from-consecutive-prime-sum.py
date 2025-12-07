class Solution:
    def isPrime(self,number):
        
        if number<2:
            return False
        div=2
        while div*div<=number:
            if number%div==0:
                return False
            div+=1
        return True
        
    def largestPrime(self, n: int) -> int:
        num=2
        sums=0
        ans=0
        while sums<=n:
            if self.isPrime(num):
                sums+=num
                if sums<=n and self.isPrime(sums):
                    ans=sums
            num+=1
        return ans
        