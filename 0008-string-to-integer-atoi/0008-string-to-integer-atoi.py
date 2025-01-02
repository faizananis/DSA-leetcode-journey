class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign=0
        result=0
        flag=0
        print(s)
        for c in s:
            if c=='-' and flag==0:
                sign=1
                flag=1
            elif c=='+' and flag==0:
                sign=0
                flag=1
            elif c>='0' and c<='9':
                result=result*10+int(c)
                flag=1
            else:
                break
        if sign==1:
            result*=-1
        if result<-2**31:
            return -2**31
        elif result>2**31-1:
            return 2**31-1
        return result


            