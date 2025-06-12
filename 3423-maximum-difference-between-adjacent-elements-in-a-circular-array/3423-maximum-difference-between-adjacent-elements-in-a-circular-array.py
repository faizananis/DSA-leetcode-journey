class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff=0
        maxDiff=0
        n=len(nums)
        for i in range(1,n+1):
            index=i%n
            diff=abs(nums[index]-nums[i-1])
            maxDiff=max(maxDiff,diff)
        return maxDiff