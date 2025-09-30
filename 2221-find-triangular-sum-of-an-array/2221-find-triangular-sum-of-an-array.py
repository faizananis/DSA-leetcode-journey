class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for _ in range(len(nums)-1):
            new_nums=[]
            i=1
            while i<len(nums):
                val=nums[i-1]+nums[i]
                new_nums.append(val%10)
                i+=1
            nums=new_nums
            print(nums)
        return nums[0]