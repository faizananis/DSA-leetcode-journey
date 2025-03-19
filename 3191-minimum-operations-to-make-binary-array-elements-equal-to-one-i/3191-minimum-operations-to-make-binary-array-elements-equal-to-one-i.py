class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]==0 and i+3>len(nums):
                return -1
            if nums[i]==0:
                for j in range(i,i+3):
                    nums[j]^=1
                count+=1
        return count
                