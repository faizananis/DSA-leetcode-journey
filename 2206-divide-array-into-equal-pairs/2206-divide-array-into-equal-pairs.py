class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        my_dict={}
        count=0
        for n in nums:
            if n in my_dict:
                my_dict[n]+=1
            else:
                my_dict[n]=1
            if my_dict[n]==2:
                count+=1
                my_dict[n]=0
        if count==len(nums)//2:
            return True
        return False