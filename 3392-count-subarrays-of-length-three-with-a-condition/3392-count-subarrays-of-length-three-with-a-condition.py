class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        left=0
        sums=0
        count=0
        for right in range(2,len(nums)):
            if nums[left]+nums[right]==nums[right-1]//2 and nums[right-1]%2==0:
                count+=1
            left+=1
        return count
            