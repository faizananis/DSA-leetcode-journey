class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxi=0
        diff=0
        result=0
        for i in range(len(nums)):
            result=max(result,diff*nums[i])
            diff=max(diff,maxi-nums[i])
            maxi=max(maxi,nums[i])
        return result
            