class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        suffix=[0]*len(nums)
        result=[0]*len(nums)
        product1=1
        for i in range(len(nums)):
            product1*=nums[i]
            prefix[i]=product1
        product2=1
        for i in range(len(nums)-1,-1,-1):
            product2*=nums[i]
            suffix[i]=product2
        result[0]=suffix[1]
        result[-1]=prefix[len(nums)-2]
        for j in range(1,len(nums)-1):
            result[j]=prefix[j-1]*suffix[j+1]
        return result
