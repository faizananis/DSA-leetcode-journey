class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi=0
        for n in nums:
            if n==1:
                count+=1
            else:
                count=0
            maxi=max(maxi,count)
        return maxi