class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq=[0]*101
        count=0
        for i in nums:
            freq[i]+=1
        for j in freq:
            if j>0:
                count=count+(j*(j-1))//2
        return count