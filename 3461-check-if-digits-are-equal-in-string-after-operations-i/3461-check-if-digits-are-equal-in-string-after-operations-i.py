class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            arr=[]
            for i in range(len(s)-1):
                summ=int(s[i])+int(s[i+1])
                val=summ%10
                arr.append(val)
            s=arr
        if s[0]==s[1]:
            return True
        return False