class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans=[]
        result=0
        while low<=high:
            sum1=0
            sum2=0
            st=str(low)
            if len(st)%2==1:
                low+=1
                continue
            first=int(st[:len(st)//2])
            last=int(st[len(st)//2:])
            while first:
                sum1+=first%10
                first//=10
            while last:
                sum2+=last%10
                last//=10
            if sum1==sum2:
                result+=1
                ans.append(low)
            low+=1
        return result