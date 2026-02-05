class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result=[]
        index=0
        for i in range(len(nums)):
            index=i
            if nums[i]>=0:
                index+=nums[i]
                index%=len(nums)
            elif nums[i]<0:
                index-=(nums[i]*-1)
                index%=len(nums)
            result.append(nums[index])
        return result