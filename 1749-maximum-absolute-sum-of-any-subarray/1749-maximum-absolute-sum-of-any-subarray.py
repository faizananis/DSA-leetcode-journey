class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        currSum=0
        maxSum=0
        for n in nums:
            currSum+=n
            maxSum=max(currSum,maxSum)
            if currSum<0:
                currSum=0
        result=maxSum
        currSum=0
        minSum=0
        for n in nums:
            currSum+=n
            minSum=min(currSum,minSum)
            if currSum>0:
                currSum=0
        result=max(abs(result),abs(minSum))
        return result