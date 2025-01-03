class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        countSplit=0
        rightSum=sum(nums)
        leftSum=0
        for i in range(len(nums)-1):
            leftSum+=nums[i]
            if leftSum>=rightSum-leftSum:
                countSplit+=1
        return countSplit