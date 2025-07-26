class Solution:
    def maxSum(self, nums: List[int]) -> int:
        neg=float("-inf")
        s=set()
        sums=0
        for i in range(len(nums)):
            if nums[i]<0:
                neg=max(neg,nums[i])
            elif nums[i] not in s:
                sums+=nums[i]
                s.add(nums[i])
        return sums if len(s)>0 else neg