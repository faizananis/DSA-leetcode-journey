class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half=len(nums)//2+1
        nums.sort()
        freq=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                freq+=1
            else:
                freq=1
            if freq>=half:
                return nums[i]
        return nums[0]