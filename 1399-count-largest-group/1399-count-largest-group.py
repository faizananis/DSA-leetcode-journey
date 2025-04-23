class Solution:
    def countLargestGroup(self, n: int) -> int:
        my_dict={}
        max_size=0
        for i in range(1,n+1):
            num=i
            sums=0
            while num:
                sums+=(num%10)
                num//=10
            if sums not in my_dict:
                my_dict[sums]=1
            else:
                my_dict[sums]+=1
            max_size=max(max_size,my_dict[sums])
        
        count=0
        for n in my_dict:
            if my_dict[n]==max_size:
                count+=1
        return count