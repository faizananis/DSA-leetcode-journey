class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        left=0
        right=0
        ans=0
        for right in range(len(nums)):
            if nums[right]-nums[left]>2*k:
                left+=1
            else:
                ans=max(ans,right-left+1)
        return ans