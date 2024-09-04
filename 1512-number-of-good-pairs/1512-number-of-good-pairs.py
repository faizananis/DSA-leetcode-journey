class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq=[0]*101
        count=0
        for i in nums:
            if i in range(len(nums)):
                freq[nums[i]]+=1
        for i in freq:
            if i!=0:
                count+=((i*(i-1)))//2
        return count