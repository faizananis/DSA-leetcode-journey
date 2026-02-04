class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        flag=False
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                flag=True
            elif flag==True and nums[i]<nums[i+1]:
                return True
        return False