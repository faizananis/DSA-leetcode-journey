class Solution:
    def reverse(self, x: int) -> int:
        flag=False
        if x<0:
            flag=True
            x*=-1
        result=0
        while x:
            result*=10
            result+=x%10
            x//=10
        if result>2147483648:
            return 0
        if flag==True:
            return -result
        return result
