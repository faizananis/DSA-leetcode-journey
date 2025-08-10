class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num={}
        digit=0
        count1=0
        while n:
            digit=n%10
            if digit not in num:
                num[digit]=1
            else:
                num[digit]+=1
            n//=10
            count1+=1
        i=0
        while 1:
            val=2**i
            count2=0
            my_dict={}
            while val:
                digit=val%10
                if digit not in my_dict:
                    my_dict[digit]=1
                else:
                    my_dict[digit]+=1
                count2+=1
                val//=10
            if count2>count1:
                break
            if my_dict==num:
                return True
            i+=1
        return False

