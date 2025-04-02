class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        value=0
        maxval=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    value=(nums[i]-nums[j])*nums[k]
                    maxval=max(maxval,value)
        if maxval<0:
            return 0
        return maxval