class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        val1=0
        val2=0
        i=1
        while True:
            val1=n-i
            val2=i
            temp1=val1
            while temp1:
                check=temp1%10
                if check==0:
                    break
                temp1//=10
            temp2=val2
            while temp2:
                check=temp2%10
                if check==0:
                    break
                temp2//=10
            if not(temp1 or temp2):
                return [val1,val2]
            i+=1
