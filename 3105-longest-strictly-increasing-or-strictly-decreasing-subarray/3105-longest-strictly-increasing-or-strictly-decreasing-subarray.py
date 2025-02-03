class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxSize=0
        size=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                size+=1
            else:
                size=0
            maxSize=max(maxSize,size+1)
        size=0
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                size+=1
            else:
                size=0
            maxSize=max(maxSize,size+1)
        if maxSize==0:
            return 1
        return maxSize
            