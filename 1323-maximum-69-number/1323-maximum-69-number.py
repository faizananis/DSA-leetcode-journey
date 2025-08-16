class Solution:
    def maximum69Number (self, num: int) -> int:
        maximum=0
        digit=0
        arr=[]
        while num:
            arr.append(num%10)
            num//=10
        arr.reverse()
        for i in range(len(arr)):
            if arr[i]==6:
                digit=9
            else:
                digit=6
            temp1=0
            temp2=0
            for j in range(len(arr)):
                temp1*=10
                temp2*=10
                temp1+=arr[j]
                if j==i:
                    temp2+=digit
                else:
                    temp2+=arr[j]
            val=max(temp1,temp2)
            maximum=max(maximum,val)
        return maximum


        
