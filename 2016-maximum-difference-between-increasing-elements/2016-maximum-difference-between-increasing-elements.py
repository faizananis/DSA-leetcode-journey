class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff=-1
        first=nums[0]
        second=0
        for i in range(1,len(nums)):
            second=nums[i]
            if second-first>0:
                maxDiff=max(maxDiff,second-first)
            first=min(first,nums[i])
        return maxDiff