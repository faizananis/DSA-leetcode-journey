class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        zero=0
        nonZero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[nonZero]=nums[i]
                nonZero+=1
            else:
                zero+=1
        while nonZero<len(nums):
            nums[nonZero]=0
            nonZero+=1
        return nums
