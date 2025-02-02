class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                break
            if target<nums[mid]:
                right=mid-1
            elif target>nums[mid]:
                left=mid+1
        if left>right:
            return [-1,-1]
        start=mid-1
        while start>=0 and nums[start]==nums[mid]:
            start-=1
        last=mid+1
        while last<len(nums) and nums[last]==nums[mid]:
            last+=1
        return [start+1,last-1]

