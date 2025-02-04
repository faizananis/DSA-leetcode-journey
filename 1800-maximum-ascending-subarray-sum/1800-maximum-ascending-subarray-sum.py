class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sums=nums[0]
        maxSum=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                sums+=nums[i]
            else:
                sums=nums[i]
            maxSum=max(maxSum,sums)
        return maxSum